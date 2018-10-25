from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify
from app.users.forms.login import LoginForm
from app.users.forms.register import RegisterForm
from app import bcrypt, db
from app.users.models.user import User

users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if (request.method=='POST'):
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data,
                        email=form.email.data,
                        password=hashed_password,
                        firstname=form.first_name.data,
                        lastname=form.last_name.data)
            db.session.add(user)
            db.session.commit()
            return jsonify({'success': True})
        else:
            return jsonify(errors=form.errors), 422
    else:
        return render_template('users/register.html', title='Register', form=form)


@users_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('users/login.html', title='Login', form=form)


