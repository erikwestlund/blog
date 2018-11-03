from flask import jsonify
from flask.views import MethodView
from flask_login import current_user, user_logged_in
from users.tasks.email_registration_confirmation import email_registration_confirmation

class ConfirmEmailRequest(MethodView):

    def post(self):
        if user_logged_in:
            email_registration_confirmation.delay(current_user.id)
            return jsonify({'success': True})
        else:
            return jsonify(errors={
                    'user': ['You must be logged in.']
                }), 422