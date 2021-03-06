from flask import Blueprint
from posts.models.post import Post
from posts.views.create import CreatePost
from posts.views.edit import EditPost, FetchPost
from posts.views.render_preview import RenderPreview
from posts.views.revisions import Revisions
from posts.views.tagged_posts import FetchTaggedPosts, ShowTaggedPosts
from posts.views.unpublish import UnpublishPost
from posts.views.admin import Index, FetchAdminPosts
from posts.views.index import FetchPosts

from posts.views.show import ShowPost

posts = Blueprint("posts", __name__, template_folder="templates")

posts.add_url_rule(
    "/admin/posts/<int:post_id>.json", view_func=FetchPost.as_view("fetch_admin_post")
)
posts.add_url_rule(
    "/admin/posts/<int:post_id>/unpublish",
    view_func=UnpublishPost.as_view("unpublish_post"),
)

posts.add_url_rule(
    "/admin/posts/render-preview", view_func=RenderPreview.as_view("render_preview")
)

posts.add_url_rule(
    "/admin/posts/<int:post_id>", view_func=EditPost.as_view("edit_post")
)

posts.add_url_rule("/admin/posts/create", view_func=CreatePost.as_view("create_post"))
posts.add_url_rule(
    "/admin/posts.json", view_func=FetchAdminPosts.as_view("fetch_admin_posts")
)
posts.add_url_rule("/admin/posts", view_func=Index.as_view("post_index"))

posts.add_url_rule("/posts.json", view_func=FetchPosts.as_view("get_posts"))

posts.add_url_rule(
    "/<int:year>/<int:month>/<string:slug>", view_func=ShowPost.as_view("show_post")
)

posts.add_url_rule(
    "/posts/tags/<string:slug>", view_func=ShowTaggedPosts.as_view("show_tagged_posts")
)
posts.add_url_rule(
    "/posts/tags/<string:slug>/posts.json",
    view_func=FetchTaggedPosts.as_view("fetch_tagged_posts"),
)

posts.add_url_rule(
    "/admin/posts/<int:post_id>/revisions", view_func=Revisions.as_view("revisions")
)
