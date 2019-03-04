from flask import jsonify, request
from flask.views import MethodView
from slugify import slugify

from app import db
from main.forms.tag import TagForm
from main.models.tag import Tag
from utils.acl import user_has_role
from utils.models.first_or_create import first_or_create


class Tags(MethodView):
    @user_has_role("writer")
    def get(self):
        search_input = request.args.get("q")
        tags = Tag.query.filter(Tag.name.contains(search_input)).all()
        return jsonify({"data": tags})

    @user_has_role("writer")
    def post(self):
        form = TagForm()
        tag = first_or_create(
            db.session, Tag, name=form.tag.data, slug=slugify(form.tag.data)
        )

        return jsonify(tag)
