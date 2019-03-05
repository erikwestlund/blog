from flask import render_template, abort, jsonify
from flask.views import MethodView
from flask_login import login_required

from app import db
from main.models.image import Image
from posts.models.post import Post
from utils.models.find_or_fail import find_or_fail


class Images(MethodView):
    def delete(self, image_id):
        image = find_or_fail(Image, Image.id == image_id)

        db.session.delete(image)
        db.session.commit()

        return jsonify({
            "data": {
                "image": image
            }
        })
