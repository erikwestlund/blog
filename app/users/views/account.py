from flask import url_for, flash, redirect, render_template
from flask.views import MethodView
from flask_login import current_user, login_required
from users.forms.account import UpdateAccountForm
from flask import jsonify
from app import db, bcrypt
from utils.acl import user_has_role
from users.models.role import Role

class Account(MethodView):

    @login_required
    @user_has_role(role='administrator')
    def get(self):
        possible_roles = Role.query.all()
        return render_template('users/account.html', user=current_user,
                               possible_roles=possible_roles)

    def post(self):
        form = UpdateAccountForm()
        if form.validate_on_submit():
            user = self.update_user(form)

            return jsonify({
                'success': True,
                'user': {
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                }
            })
        else:
            return jsonify(errors=form.errors), 422

        return 'true'

    def update_user(self, form):
        user = current_user
        user.username = form.username.data
        user.email = form.email.data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data

        if form.password.data:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user.password = hashed_password

        db.session.commit()

        return user
