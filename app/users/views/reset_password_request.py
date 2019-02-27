from flask import render_template, jsonify, flash
from flask.views import MethodView
from users.models.user import User
from users.tasks.email_reset_password_link import email_reset_password_link

from users.forms.reset_password_request import ResetPasswordRequestForm


class ResetPasswordRequest(MethodView):
    def get(self):
        return render_template("users/reset_password_request.html")

    def post(self):
        form = ResetPasswordRequestForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()

            email_reset_password_link.delay(user.id)

            flash(
                "We have sent you an email with directions on how to reset your password."
            )
            return jsonify({"success": True})
        else:
            return jsonify(errors=form.errors), 422
