from flask import abort, jsonify
from flask import render_template
from flask.views import MethodView
from flask_login import current_user, login_required
from funcy import lpluck_attr

from app import db, bcrypt
from users.forms.account import UpdateAccountForm
from users.models.role import Role
from users.models.user import User
from utils.models.find_or_fail import find_or_fail


class Account(MethodView):
    @login_required
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
        else:
            user = current_user

        if not self.has_permission(user):
            abort(403)

        own_account = True if user == current_user else False

        possible_user_roles = Role.jsonify(Role.query.all())
        user_roles = lpluck_attr("id", user.roles)
        return render_template(
            "users/account.html",
            user=user,
            user_roles=user_roles,
            own_account=own_account,
            possible_user_roles=possible_user_roles,
        )

    @login_required
    def patch(self, user_id):
        user = find_or_fail(User, user_id == User.id)

        if not self.has_permission(user):
            abort(403)

        form = UpdateAccountForm(user_being_edited=user)
        if form.validate_on_submit():
            updated_user = self.update_user(user, form)

            return jsonify(
                {
                    "success": True,
                    "user": {
                        "username": updated_user.username,
                        "email": updated_user.email,
                        "first_name": updated_user.first_name,
                        "last_name": updated_user.last_name,
                    },
                }
            )
        else:
            return jsonify(errors=form.errors), 422

        return "true"

    def has_permission(self, user):
        if user == current_user:
            return True
        else:
            return current_user.has_role("administrator")

    def update_user(self, user, form):
        user.username = form.username.data
        user.email = form.email.data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data

        if current_user.has_role("administrator"):
            roles = Role.query.filter(Role.id.in_(form.user_roles.data)).all()
            user.roles.extend(roles)

        if form.password.data:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
                "utf-8"
            )
            user.password = hashed_password

        db.session.commit()

        return user
