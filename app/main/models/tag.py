from app import db
from utils.models.timestamps import TimestampMixin


class Tag(db.Model, TimestampMixin):

    visible = ["id", "name"]

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, server_default="", unique=True)
    posts = db.relationship("Tag", back_populates="posts", secondary="tag_post")

    def __repr__(self):
        return f"Tag('{self.name}')"
