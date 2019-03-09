from flask import render_template, jsonify
from flask.views import MethodView
from flask_login import login_required

from app import db
from main.models.image import Image
from pages.forms.save_page import SavePageForm
from pages.models.page import Page
from utils.acl import user_has_role


class CreatePage(MethodView):
    @user_has_role("administrator")
    def get(self):
        return render_template("pages/create.html", title="Create Page")

    @user_has_role("administrator")
    def post(self):
        form = SavePageForm()

        if form.validate_on_submit():
            page = Page(
                title=form.title.data,
                slug=form.slug.data,
                body=form.body.data,
                primary_image_id=form.primary_image_id.data or None
            )

            page.images = Image.query.filter(
                Image.id.in_(form.uploaded_images.data)
            ).all()

            db.session.add(page)
            db.session.commit()

            return jsonify({"action": "create", "success": True, "page": page})
        else:
            return jsonify(errors=form.errors), 422
