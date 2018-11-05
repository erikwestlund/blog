from flask import render_template, request, jsonify
from flask.views import MethodView
from utils.requests import request_wants_json
from users.models.user import User


class AdminUsersIndex(MethodView):

    def get(self):
        return render_template('users/admin.html')


class AdminUsersIndexJson(MethodView):

    def get(self):
        return jsonify(
            User.query.order_by(User.created_at).paginate().items
        )
