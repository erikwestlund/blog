from flask import redirect, url_for, jsonify
from flask import render_template, flash
from flask.views import MethodView
from flask_login import current_user

from app import bcrypt, db
from users.forms.reset_password import ResetPasswordForm
from users.models.user import User


class ResetPassword(MethodView):
    def get(self, token):
        if current_user.is_authenticated:
            return redirect(url_for("main.index"))

        user = User.verify_token(token)

        if user is None:
            flash(
                "Invalid or expired password reset token. Request a new one below.",
                "warning",
            )
            return redirect(url_for("users.reset_password_request"))
        else:
            new_token = user.generate_password_reset_token()
            return render_template(
                "users/reset_password.html", token=new_token, title="Reset Password"
            )

    def post(self, token):
        if current_user.is_authenticated:
            return redirect(url_for("main.index"))

        user = User.verify_token(token)
        form = ResetPasswordForm()
        if form.validate_on_submit():
            user.password = bcrypt.generate_password_hash(form.password.data).decode(
                "utf-8"
            )
            db.session.commit()

            flash("Your password has been reset!", "success")

            return jsonify({"success": True})
        else:
            errors = form.errors
            if user is None:
                errors["token"] = ["Invalid token."]

            return jsonify(errors=form.errors), 422
