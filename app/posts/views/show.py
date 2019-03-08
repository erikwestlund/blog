from flask import render_template, abort
from flask.views import MethodView
from flask_login import login_required
from posts.models.post import Post


class ShowPost(MethodView):
    def get(self, year, month, slug):
        post = Post.get_posts_query_by_slug_within_month(slug, year, month).first()

        if not post:
            abort(404)

        return render_template("posts/show.html", post=post,
                               title=post.title,
                               og_type="article",
                               og_type_published=post.published_at.isoformat() or None,
                               og_type_modified=post.updated_at.isoformat() or None ,
                               og_type_tag=','.join([tag.name for tag in post.tags]) if post.tags else None,
                               og_type_author=post.user.name)
