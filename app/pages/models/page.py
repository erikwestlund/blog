from flask import url_for
from markdown2 import Markdown
from slugify import slugify
from sqlalchemy import ForeignKey

from app import db
from utils.models.timestamps import TimestampMixin

image_page = db.Table(
    "image_page",
    db.Column("image_id", db.Integer(), db.ForeignKey("image.id")),
    db.Column("page_id", db.Integer(), db.ForeignKey("page.id")),
)

class Page(db.Model, TimestampMixin):
    visible = [
        "id",
        "title",
        "slug",
        "body",
        "body_html",
        "created_at",
        "updated_at",
        "images",
        "primary_image",
        "url",
        "edit_url",
    ]

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, server_default="")
    body = db.Column(db.Text(), nullable=False, server_default="")
    slug = db.Column(db.Text())
    primary_image_id = db.Column(db.Integer, ForeignKey("image.id"), nullable=True)

    # Relationships
    images = db.relationship(
        "Image", secondary=image_page, cascade="save-update"
    )
    primary_image = db.relationship("Image")

    revisions = db.relationship("PageRevision", backref="page", lazy=True)


    @property
    def uri(self):
        return '/' + self.slug

    @property
    def url(self):
        return url_for("main.index", _external=True) + self.uri

    @property
    def edit_uri(self):
        return "admin/pages/%s" % self.id

    @property
    def edit_url(self):
        return url_for("main.index") + self.edit_uri

    @property
    def body_html(self):
        return Page.convert_markdown_to_html(self.body)

    @staticmethod
    def convert_markdown_to_html(markdown):
        return Markdown(extras=["markdown-in-html"]).convert(markdown)

    @staticmethod
    def generate_slug(title, published_at):
        return slugify(title)

    def __repr__(self):
        return f"Page('{self.title}, {self.body}, {self.slug}')"


class PageRevision(db.Model, TimestampMixin):
    visible = ["id", "page_id", "revision"]

    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey("page.id"))
    revision = db.Column(db.JSON)
