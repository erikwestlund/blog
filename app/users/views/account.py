from flask import jsonify
from flask import render_template
from flask.views import MethodView
from flask_login import current_user, login_required
from funcy import lpluck_attr

from app import db, bcrypt
from users.forms.account import UpdateAccountForm
from users.models.role import Role
from utils.acl import user_has_role


class Account(MethodView):

    @login_required
    def get(self):
        user_roles = lpluck_attr('id', current_user.roles)
        possible_user_roles = Role.listify(Role.query.all())
        return render_template('users/account.html',
                               user=current_user,
                               user_roles=user_roles,
                               possible_user_roles=possible_user_roles)

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

        if current_user.has_role('administrator'):
            roles = Role.query.filter(Role.id.in_(form.user_roles.data)).all()
            user.roles = []
            user.roles.extend(roles)

        if form.password.data:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user.password = hashed_password

        db.session.commit()

        return user
