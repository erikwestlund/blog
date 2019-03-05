from flask import url_for
from sqlalchemy.ext.hybrid import hybrid_property

from app import db
from utils.models.timestamps import TimestampMixin


class Tag(db.Model, TimestampMixin):

    visible = ["id", "name", "post_url"]

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, server_default="", unique=True)
    posts = db.relationship("Tag", back_populates="posts", secondary="tag_post")
    slug = db.Column(db.Text())

    @property
    def post_uri(self):
        return "posts/tags/%s" % self.slug

    @property
    def post_url(self):
        return url_for("main.index") + self.post_uri

    def __repr__(self):
        return f"Tag('{self.name}')"
