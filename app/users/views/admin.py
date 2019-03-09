from flask import render_template, request
from flask.views import MethodView
from flask_login import login_required

from users.models.user import User
from utils.models.paginated_json_response import paginated_json_response
from utils.acl import user_has_role
from flask import current_app


class AdminUsersIndex(MethodView):
    @user_has_role("administrator")
    def get(self):
        return render_template("users/index.html", title="Users Administration")


class AdminUsersIndexJson(MethodView):
    @user_has_role("administrator")
    def get(self):
        per_page = int(current_app.config["PAGINATE_DEFAULT"])

        page = int(request.args.get("page")) if request.args.get("page") else 1
        return paginated_json_response(User, per_page=per_page, page=page)
