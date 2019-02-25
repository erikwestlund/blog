from flask import abort
from flask import jsonify
from flask.views import MethodView
from flask_login import current_user
from flask_login import login_required

from posts.models.post import Post


class FetchPost(MethodView):

    @login_required
    def get(self, post_id):
        post = Post.query.get(post_id)

        if not current_user.has_role('administrator') or current_user.id != post.user_id:
            abort(403)

        return jsonify({
            'data': post.to_dict()
        })
