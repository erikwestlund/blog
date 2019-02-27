from flask import Blueprint
from posts.models.post import Post
from posts.views.create import CreatePost
from posts.views.edit import EditPost, FetchPost
from posts.views.unpublish import UnpublishPost
from posts.views.index import Index, FetchPosts

posts = Blueprint("posts", __name__, template_folder="templates")

posts.add_url_rule(
    "/admin/posts/<int:post_id>.json", view_func=FetchPost.as_view("fetch_post")
)
posts.add_url_rule(
    "/admin/posts/<int:post_id>/unpublish",
    view_func=UnpublishPost.as_view("unpublish_post"),
)
posts.add_url_rule(
    "/admin/posts/<int:post_id>", view_func=EditPost.as_view("edit_post")
)
posts.add_url_rule("/admin/posts/create", view_func=CreatePost.as_view("create_post"))
posts.add_url_rule("/admin/posts.json", view_func=FetchPosts.as_view("fetch_posts"))
posts.add_url_rule("/admin/posts", view_func=Index.as_view("post_index"))
