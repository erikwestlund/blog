from flask import render_template, request
from flask.views import MethodView
from flask_login import login_required, current_user
from flask import current_app
from utils.models.paginated_json_response import paginated_json_response
from posts.models.post import Post


class FetchPosts(MethodView):
    @login_required
    def get(self):
        per_page = int(current_app.config["PAGINATE_DEFAULT"])

        page = int(request.args.get("page")) if request.args.get("page") else 1

        user_id = (
            current_user.id if not current_user.has_role("administrator") else None
        )

        return paginated_json_response(
            Post,
            per_page=per_page,
            page=page,
            user_id=user_id,
            order_by="created_at",
            order_by_direction="desc",
        )


class Index(MethodView):
    @login_required
    def get(self):
        return render_template("posts/index.html")
