from flask import render_template
from flask.views import MethodView
from flask_login import login_required

from users.models.user import User
from utils.models.paginated_json_response import paginated_json_response
from utils.acl import user_has_role

class AdminUsersIndex(MethodView):

    @user_has_role('administrator')
    def get(self):
        return render_template('users/admin.html')


class AdminUsersIndexJson(MethodView):

    @user_has_role('administrator')
    def get(self):
        return paginated_json_response(User, per_page=1, page=1)
