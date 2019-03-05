from sqlalchemy.ext.hybrid import hybrid_property

from app import db
from utils.models.timestamps import TimestampMixin


class Image(db.Model, TimestampMixin):

    visible = ["id", "url", "width", "height"]

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text(), nullable=False)
    width = db.Column(db.Integer(), nullable=True)
    height = db.Column(db.Integer(), nullable=True)
    cloudinary_public_id = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"Image('{self.url}')"
