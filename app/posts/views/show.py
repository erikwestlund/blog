from flask import render_template, abort
from flask.views import MethodView
from flask_login import login_required
from posts.models.post import Post


class ShowPost(MethodView):
    @login_required
    def get(self, year, month, slug):
        post = Post.get_posts_query_by_slug_within_month(slug, year, month).first()

        if not post:
            abort(404)

        return render_template("posts/show.html", post=post)
