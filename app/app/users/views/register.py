from app import bcrypt, db
from app.users.forms.register import RegisterForm
from app.users.models.user import User
from app.users.tasks.email_registration_confirmation import email_registration_confirmation
from flask import render_template, flash, jsonify
from flask.views import MethodView

class Register(MethodView):

    def get(self):
        return render_template('users/register.html', title='Register')

    def post(self):
        form = RegisterForm()
        if form.validate_on_submit():
            user = save_new_user(form)

            email_registration_confirmation.delay(user.id)

            flash('A confirmation email has been sent.')
            return jsonify({'success': True})
        else:
            return jsonify(errors=form.errors), 422


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
