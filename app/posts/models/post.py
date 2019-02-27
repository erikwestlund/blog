from app import db
from utils.models.timestamps import TimestampMixin
from sqlalchemy import ForeignKey

tag_post = db.Table(
    "tag_post",
    db.Column("tag_id", db.Integer(), db.ForeignKey("tag.id")),
    db.Column("post_id", db.Integer(), db.ForeignKey("post.id")),
)


class Post(db.Model, TimestampMixin):
    visible = [
        "id",
        "user_id",
        "title",
        "body",
        "created_at",
        "updated_at",
        "published_at",
        "tags",
        "user",
    ]

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("user.id"))
    title = db.Column(db.String(255), nullable=False, server_default="")
    body = db.Column(db.Text(), nullable=False, server_default="")
    published_at = db.Column(db.DateTime())

    # Relationships
    user = db.relationship("User")
    tags = db.relationship(
        "Tag",
        secondary=tag_post,
        lazy="dynamic",
        cascade="save-update",
        backref=db.backref("posts", lazy="dynamic"),
    )

    revisions = db.relationship("PostRevision", backref="post", lazy=True)

    def __repr__(self):
        return f"Post('{self.title}, {self.body}')"


class PostRevision(db.Model, TimestampMixin):
    visible = ["id", "post_id", "revision"]

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    revision = db.Column(db.JSON)
