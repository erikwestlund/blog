from flask import current_app
from flask import request
from flask.views import MethodView

from posts.models.post import Post
from utils.models.paginated_json_response import paginated_json_response


class FetchPosts(MethodView):
    def get(self):
        per_page = int(current_app.config["POSTS_PER_PAGE"])

        page = int(request.args.get("page")) if request.args.get("page") else 1

        return paginated_json_response(
            Post,
            per_page=per_page,
            page=page,
            order_by="created_at",
            order_by_direction="desc",
        )
