from sqlalchemy.ext.hybrid import hybrid_property

from app import db
from slugify import slugify
from sqlalchemy import ForeignKey
from sqlalchemy import and_
from markdown2 import Markdown
from utils.striphtmltags import MLStripper

from utils.models.timestamps import TimestampMixin
from dateutil.parser import parse as parse_date
import datetime
import calendar

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
        "slug",
        "body",
        "body_md",
        "created_at",
        "updated_at",
        "published_at",
        "tags",
        "user",
        "url",
    ]

    snippet_length = 500

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("user.id"))
    title = db.Column(db.String(255), nullable=False, server_default="")
    body = db.Column(db.Text(), nullable=False, server_default="")
    published_at = db.Column(db.DateTime())
    slug = db.Column(db.Text())

    # Relationships
    user = db.relationship("User")

    tags = db.relationship(
        "Tag",
        secondary=tag_post,
        lazy="dynamic",
        cascade="save-update, merge, delete",
        backref=db.backref("posts", lazy="dynamic"),
    )

    revisions = db.relationship("PostRevision", backref="post", lazy=True)

    @hybrid_property
    def published_at_display(self):
        return (
            self.published_at.strftime("%B %-d, %Y at %I:%M %p")
            if self.published_at
            else None
        )

    @hybrid_property
    def url(self):
        if not self.published_at:
            return None

        year = self.published_at.year
        month = str(self.published_at.month).zfill(2)

        return "%d/%s/%s" % (year, month, self.slug)

    @hybrid_property
    def body_md(self):
        return Markdown().convert(self.body)

    @staticmethod
    def generate_slug(title, published_at):
        initial_slug = slug = slugify(title)
        slug_version = 1

        while Post.slug_exists_within_month(slug, published_at):
            slug = "%s-%d" % (initial_slug, slug_version)
            slug_version += 1

        return slug

    @staticmethod
    def slug_exists_within_month(slug, published_at):
        date = parse_date(published_at)
        year = date.year
        month = date.month

        return Post.get_posts_query_by_slug_within_month(slug, year, month).count() > 0

    @hybrid_property
    def snippet(self):
        return self.body_md[: self.snippet_length]

    @staticmethod
    def get_posts_query_by_slug_within_month(slug, year, month):
        num_days = calendar.monthrange(year, month)[1]
        start_date = datetime.datetime(year, month, 1, 0, 0, 0)
        end_date = datetime.datetime(year, month, num_days, 23, 59, 59)

        return Post.query.filter(
            and_(Post.published_at >= start_date, Post.published_at <= end_date)
        ).filter_by(slug=slug)

    def __repr__(self):
        return f"Post('{self.title}, {self.body}, {self.slug}')"


class PostRevision(db.Model, TimestampMixin):
    visible = ["id", "post_id", "revision"]

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    revision = db.Column(db.JSON)
