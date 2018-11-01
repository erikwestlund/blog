from flask import url_for, flash, redirect
from flask.views import MethodView
from flask_login import logout_user


class Logout(MethodView):

    def get(self):
        logout_user()
        flash('You have been logged out.')
        return redirect(url_for('main.home'))
