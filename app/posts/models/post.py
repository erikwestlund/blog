import calendar
import datetime

from dateutil.parser import parse as parse_date
from flask import current_app, url_for
from flask_login import current_user
from markdown2 import Markdown
from slugify import slugify
from sqlalchemy import ForeignKey
from sqlalchemy import and_
from main.models.image import Image

from app import db
from utils.models.timestamps import TimestampMixin
from utils.striphtmltags import strip_tags

tag_post = db.Table(
    "tag_post",
    db.Column("tag_id", db.Integer(), db.ForeignKey("tag.id")),
    db.Column("post_id", db.Integer(), db.ForeignKey("post.id")),
)

image_post = db.Table(
    "image_post",
    db.Column("image_id", db.Integer(), db.ForeignKey("image.id")),
    db.Column("post_id", db.Integer(), db.ForeignKey("post.id")),
)


class Post(db.Model, TimestampMixin):
    visible = [
        "id",
        "user_id",
        "title",
        "slug",
        "body",
        "body_html",
        "body_snippet",
        "created_at",
        "updated_at",
        "published_at",
        "tags",
        "images",
        "user",
        "url",
        "edit_url",
        "editable",
    ]

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("user.id"))
    title = db.Column(db.String(255), nullable=False, server_default="")
    body = db.Column(db.Text(), nullable=False, server_default="")
    published_at = db.Column(db.DateTime())
    slug = db.Column(db.Text())

    # Relationships
    user = db.relationship("User", lazy="joined", innerjoin=True)

    tags = db.relationship(
        "Tag", secondary=tag_post, cascade="save-update, merge, delete"
    )

    images = db.relationship(
        "Image", secondary=image_post, cascade="save-update, merge, delete"
    )

    revisions = db.relationship("PostRevision", backref="post", lazy=True)

    @property
    def owner(self):
        return self.user

    @property
    def editable(self):
        if not current_user.is_authenticated:
            return False
        else:
            return (
                True
                if (
                    current_user.has_role("administrator")
                    or self.user_id == current_user.id
                )
                else False
            )

    @property
    def published_at_display(self):
        return (
            self.published_at.strftime("%B %-d, %Y at %I:%M %p")
            if self.published_at
            else None
        )

    @property
    def uri(self):
        if not self.published_at:
            return None

        year = self.published_at.year
        month = str(self.published_at.month).zfill(2)

        return "%d/%s/%s" % (year, month, self.slug)

    @property
    def url(self):
        return url_for("main.index") + self.uri if self.published_at else None

    @property
    def edit_uri(self):
        return "admin/posts/%s" % self.id if self.editable else None

    @property
    def edit_url(self):
        return url_for("main.index") + self.edit_uri if self.editable else None

    @property
    def body_html(self):
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

    @property
    def body_snippet(self):
        snippet_length = int(current_app.config["POST_SNIPPET_LENGTH"])
        stripped_html = strip_tags(self.body_html)

        return (
            stripped_html
            if len(stripped_html) <= snippet_length
            else stripped_html[:snippet_length] + "..."
        )

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
