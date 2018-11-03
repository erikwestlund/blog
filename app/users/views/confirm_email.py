import datetime

from app import db
from users.models.user import User
from flask import url_for, flash, redirect
from flask.views import MethodView
from flask_login import current_user


class ConfirmEmail(MethodView):

    def get(self, token):
        user = User.verify_token(token)

        if user is None:
            flash('Invalid or expired email confirmation token.', 'danger')
        elif user.email_confirmed_at:
            flash('This user has already been verified.', 'warning')
        else:
            user.active = True
            user.email_confirmed_at = datetime.datetime.now()
            db.session.commit()

            flash('Your email has been verified!', 'success')

        return redirect(url_for('main.index'))