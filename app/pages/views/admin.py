from flask import render_template, request
from flask.views import MethodView
from flask_login import login_required, current_user
from flask import current_app
from utils.models.paginated_json_response import paginated_json_response
from pages.models.page import Page


class FetchAdminPages(MethodView):
    @login_required
    def get(self):
        per_page = int(current_app.config["PAGINATE_DEFAULT"])

        page = int(request.args.get("page")) if request.args.get("page") else 1

        return paginated_json_response(
            Page,
            per_page=per_page,
            page=page,
            order_by="created_at",
            order_by_direction="desc",
        )


class Index(MethodView):
    @login_required
    def get(self):
        return render_template("pages/index.html")
