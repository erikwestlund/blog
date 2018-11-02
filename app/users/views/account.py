from flask import url_for, flash, redirect, render_template
from flask.views import MethodView
from flask_login import current_user, login_required

class Account(MethodView):

    @login_required
    def get(self):

        return render_template('users/account.html', user=current_user)
