from flask import render_template, request, current_app, jsonify, flash
from flask.views import MethodView
from flask_mail import Message

from app import celery, mail
from main.forms.contact_form import ContactForm
from utils.striphtmltags import strip_tags


class Contact(MethodView):
    def get(self):
        admin_email = current_app.config["BLOG_ADMIN_EMAIL"]
        return render_template(
            "main/contact.html", admin_email=admin_email, title="Contact Me"
        )

    def post(self):
        form = ContactForm()

        if form.validate_on_submit():
            flash("Your message has been sent!")
            email_admin(form, current_app.config["BLOG_ADMIN_EMAIL"])
            return jsonify({"status": "success"})
        else:
            return jsonify(errors=form.errors), 422


@celery.task()
def email_admin(form, email):

    msg = Message(
        (current_app.config["BLOG_TITLE"] or "Blog")
        + ": Message For You From "
        + form.name.data,
        recipients=[email],
        reply_to=form.email.data,
    )
    msg.html = render_template(
        "main/contact_email.html",
        name=form.name.data,
        email=form.email.data,
        body=strip_tags(form.body.data).replace("\n", "<br />\n"),
    )
    mail.send(msg)
