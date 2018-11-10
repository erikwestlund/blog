from flask import render_template, jsonify, request
from flask.views import MethodView
from utils.acl import user_has_role
from main.models.tag import Tag

class Tags(MethodView):

    @user_has_role('writer')
    def get(self):
        search_input = request.args.get('q')
        tags = Tag.query.filter(Tag.name.contains(search_input)).all()
        return jsonify({
            'data': tags
        })

    @user_has_role('writer')
    def post(self):
        data = request.get_json()

        return jsonify(data.tag.text)