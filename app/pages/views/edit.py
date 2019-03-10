import sys
from datetime import datetime


from flask import abort, current_app
from flask import flash
from flask import render_template, jsonify
from flask.views import MethodView
from flask_login import login_required, current_user
from slugify import slugify
from sqlalchemy import func, null as sqlalchemy_null

from app import db
from main.models.image import Image
from main.models.tag import Tag
from pages.forms.save_page import SavePageForm
from pages.models.page import Page, PageRevision
from utils.acl import user_has_role
from utils.models.find_or_fail import find_or_fail


class FetchPage(MethodView):
    @user_has_role("administrator")
    def get(self, page_id):
        page = Page.query.get(page_id)

        return jsonify({"data": page.to_dict()})


class EditPage(MethodView):
    @user_has_role("administrator")
    def get(self, page_id):
        return render_template("pages/edit.html", page_id=page_id, title="Edit Page")

    @user_has_role("administrator")
    def delete(self, page_id):
        page = find_or_fail(Page, Page.id == page_id)

        db.session.delete(page)
        db.session.commit()

        flash("Page successfully deleted.")

        return jsonify({"action": "delete", "success": True, "page": page})

    @user_has_role("administrator")
    def patch(self, page_id):
        page = find_or_fail(Page, Page.id == page_id)

        form = SavePageForm(page)

        if form.validate_on_submit():
            revision = PageRevision(page_id=page_id, revision=page.to_json())
            db.session.add(revision)

            page.title = form.title.data
            page.slug = slugify(form.slug.data)
            page.body = form.body.data
            page.primary_image_id = form.primary_image_id.data

            page.images = Image.query.filter(
                Image.id.in_(form.uploaded_images.data)
            ).all()

            db.session.commit()

            return jsonify(
                {
                    "action": "edit",
                    "success": True,
                    "page": page,
                    "images": form.uploaded_images.data,
                }
            )
        else:
            return jsonify(errors=form.errors), 422
