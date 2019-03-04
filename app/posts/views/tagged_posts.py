from flask import current_app, render_template
from flask import request
from flask.views import MethodView
from main.models.tag import Tag
from sqlalchemy import desc
from sqlalchemy.sql.functions import now

from posts.models.post import Post
from utils.models.find_or_fail import find_or_fail
from utils.models.paginated_json_response import paginated_json_response


class FetchTaggedPosts(MethodView):
    def get(self, slug):
        tag = find_or_fail(Tag, Tag.slug == slug)

        per_page = int(current_app.config["POSTS_PER_PAGE"])

        page = int(request.args.get("page")) if request.args.get("page") else 1

        query = (
            Post.query.filter(Post.published_at <= now())
            .filter(Post.tags.any(slug=slug))
            .order_by(desc("published_at"))
        )

        return paginated_json_response(query=query, per_page=per_page, page=page)


class ShowTaggedPosts(MethodView):
    def get(self, slug):
        tag = find_or_fail(Tag, Tag.slug == slug)
        page = request.args.get("page") or 1

        return render_template("posts/tagged_posts.html", tag=tag, page=page)
