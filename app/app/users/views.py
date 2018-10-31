import datetime

from app import bcrypt, db
from app.users.forms.login import LoginForm
from app.users.forms.register import RegisterForm
from app.users.models import User
from app.users.tasks import email_registration_confirmation
from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify
from flask_login import logout_user, current_user, login_user

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
            user = save_new_user(form)

            email_registration_confirmation.delay(user.id)

            flash('A confirmation email has been sent.')
            return jsonify({'success': True})
        else:
            return jsonify(errors=form.errors), 422
    else:
        return render_template('users/register.html', title='Register', form=form)


def save_new_user(form):
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data,
                email=form.email.data,
                password=hashed_password,
                first_name=form.first_name.data,
                last_name=form.last_name.data)
    db.session.add(user)
    db.session.commit()
    return user


@users.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
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
    else:
        if current_user.is_authenticated:
            return redirect(url_for('main.home'))
        else:
            return render_template('users/login.html', title='Log In')


@users.route("/users/confirm-email/<token>")
def confirm_email(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    user = User.verify_reset_token(token)

    if user is None:
        flash('Invalid or expired email confirmation token.', 'danger')
    elif user.email_confirmed_at:
        flash('This user has already been verified.', 'warning')
    else:
        user.email_confirmed_at = datetime.datetime.now()
        db.session.commit()

        flash('Your email has been verified!', 'success')

    return redirect(url_for('main.home'))
