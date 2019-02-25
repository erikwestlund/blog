from flask import Blueprint
from posts.models.post import Post
from posts.views.create import CreatePost
from posts.views.edit import EditPost
from posts.views.unpublish import UnpublishPost

posts = Blueprint('posts', __name__, template_folder='templates')

posts.add_url_rule('/posts/<int:post_id>/unpublish', view_func=UnpublishPost.as_view('unpublish_post'))
posts.add_url_rule('/posts/<int:post_id>', view_func=EditPost.as_view('edit_post'))
posts.add_url_rule('/posts/create', view_func=CreatePost.as_view('create_post'))
