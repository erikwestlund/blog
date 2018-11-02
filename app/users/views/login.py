from app import bcrypt
from users.forms.login import LoginForm
from users.models.user import User
from flask import render_template, url_for, redirect, jsonify
from flask.views import MethodView
from flask_login import current_user, login_user


class Login(MethodView):

    def get(self):
        if current_user.is_authenticated:
            return redirect(url_for('main.index'))
        else:
            return render_template('users/login.html', title='Log In')

    def post(self):
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return jsonify({
                    'success': True,
                })
            else:
                return jsonify(errors={
                    'password': ['Incorrect email and password.']
                }), 422
        else:
            return jsonify(errors=form.errors), 422

