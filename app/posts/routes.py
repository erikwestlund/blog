from flask import Blueprint
from posts.models.post import Post
from posts.views.create import CreatePost

posts = Blueprint('posts', __name__, template_folder='templates')

posts.add_url_rule('/posts/create', view_func=CreatePost.as_view('create_post'))
