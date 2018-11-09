from flask import Blueprint
from posts.models.post import Post

posts = Blueprint('posts', __name__, template_folder='templates')

