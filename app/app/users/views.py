from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify
from app.users.forms.login import LoginForm
from app.users.forms.register import RegisterForm
from app import bcrypt, db
from app.users.models.user import User
from flask_login import login_user, logout_user, current_user

users = Blueprint('users', __name__, template_folder='templates')


@users.route("/logout")
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.home'))


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data,
                        email=form.email.data,
                        password=hashed_password,
                        first_name=form.first_name.data,
                        last_name=form.last_name.data)

            db.session.add(user)
            db.session.commit()

            token = user.generate_confirmation_token()

            flash('A confirmation email has been sent.' + token)
            return jsonify({'success': True})
        else:
            return jsonify(errors=form.errors), 422
    else:
        return render_template('users/register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('users/login.html', title='Login', form=form)


