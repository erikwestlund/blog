from flask import abort
from flask import jsonify
from flask.views import MethodView
from flask_login import current_user
from flask_login import login_required
from sqlalchemy import func

from app import db
from main.models.tag import Tag
from posts.forms.save_post import SavePostForm
from posts.models.post import Post, PostRevision


class UnpublishPost(MethodView):
    @login_required
    def patch(self, post_id):
        post = Post.query.get(post_id)

        if not (
            current_user.has_role("administrator") or current_user.id != post.user_id
        ):
            abort(403)

        post.published_at = None

        db.session.commit()

        return jsonify({"action": "unpublish", "success": True, "post": post})
