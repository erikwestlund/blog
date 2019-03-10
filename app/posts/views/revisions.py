from flask import jsonify, abort
from flask.views import MethodView

from posts.models.post import Post
from utils.acl import user_can_write_posts
from utils.models.find_or_fail import find_or_fail


class Revisions(MethodView):
    @user_can_write_posts
    def get(self, post_id):
        post = find_or_fail(Post, Post.id == post_id)

        if not post.editable:
            abort(403)

        return jsonify({
            "status": "success",
            "data": post.revisions,
            "parent": post,
        })


# class Revisions(MethodView):
#     @user_can_write_posts
#     def get(self, post_id):
#         pass
