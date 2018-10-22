from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify
from app.users.forms.login import LoginForm
from app.users.forms.register import RegisterForm

users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if (request.method=='POST'):
        if form.validate_on_submit():
            if form.email.data == 'admin@blog.com' and form.password.data == 'password':
                flash('You have been logged in!', 'success')
                return jsonify({
                    'status': 'success'
                })
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


