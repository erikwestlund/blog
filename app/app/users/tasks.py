from app import celery
from app.users.models.user import User
from flask_mail import Message
from app import mail
from flask import render_template, url_for

@celery.task()
def email_registration_confirmation(user_id):
    user = User.query.get(user_id)
    token = user.generate_confirmation_token()

    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.html = render_template('users/confirm_email.html', confirm_url=url_for('users.confirm_email', token=user.generate_confirmation_token()))
    mail.send(msg)