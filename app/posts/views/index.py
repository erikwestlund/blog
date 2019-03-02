from flask import current_app
from flask import request
from flask.views import MethodView
from sqlalchemy import desc
from sqlalchemy.sql.functions import now

from posts.models.post import Post
from utils.models.paginated_json_response import paginated_json_response


class FetchPosts(MethodView):
    def get(self):
        per_page = int(current_app.config["POSTS_PER_PAGE"])

        page = int(request.args.get("page")) if request.args.get("page") else 1

        query = Post.query.filter(Post.published_at <= now()).order_by(
            desc("published_at")
        )

        return paginated_json_response(query=query, per_page=per_page, page=page)
