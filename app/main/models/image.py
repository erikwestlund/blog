import os

from flask import url_for, current_app
from sqlalchemy.ext.hybrid import hybrid_property

from app import db
from utils.models.timestamps import TimestampMixin


class Image(db.Model, TimestampMixin):
    visible = ["id", "url", "width", "height"]

    id = db.Column(db.Integer, primary_key=True)

    provider = db.Column(db.String())
    bucket = db.Column(db.String())
    path = db.Column(db.Text())

    width = db.Column(db.Integer(), nullable=True)
    height = db.Column(db.Integer(), nullable=True)

    posts = db.relationship("Image", back_populates="posts", secondary="image_post")

    @property
    def url(self):
        if self.provider == "s3" and current_app.config["AWS_S3_USING_CDN"]:
            # When using a CDN, we don't need to append a bucket name, so we can just return early
            return os.path.join(current_app.config["AWS_S3_URL_BASE"], self.path)
        elif self.provider == "s3" and not current_app.config["AWS_S3_USING_CDN"]:
            url_base = current_app.config["AWS_S3_URL_BASE"]
        elif self.provider == "b2":
            url_base = current_app.config["B2_URL_BASE"]
        else:
            url_base = url_for("main.index", _external=True)

        return os.path.join(url_base, self.bucket, self.path)

    def __repr__(self):
        return f"Image('{self.url}')"
