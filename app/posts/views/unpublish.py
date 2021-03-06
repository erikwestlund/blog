from flask import abort
from flask import jsonify
from flask.views import MethodView
from flask_login import current_user

from app import db
from posts.models.post import Post
from utils.acl import user_can_write_posts


class UnpublishPost(MethodView):
    @user_can_write_posts
    def patch(self, post_id):
        post = Post.query.get(post_id)

        if not (
            current_user.has_role("administrator") or current_user.id != post.user_id
        ):
            abort(403)

        post.published_at = None

        db.session.commit()

        return jsonify({"action": "unpublish", "success": True, "post": post})
