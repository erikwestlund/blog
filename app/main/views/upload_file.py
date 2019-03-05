from flask import jsonify
from flask.views import MethodView

from app import db
from main.models.image import Image
from utils.uploads import upload_file


class UploadImageFile(MethodView):
    def post(self):
        upload = upload_file()

        if upload["status"] == "error":
            return jsonify({"data": upload}), 422

        image = Image(url=upload["data"]["url"])
        db.session.add(image)
        db.session.commit()

        return jsonify(
            {"data": {"filename": upload["data"]["original_filename"], "image": image}}
        )


class UploadFile(MethodView):
    def post(self):
        upload = upload_file()

        if upload["status"] == "error":
            return jsonify({"data": upload}), 422

        return jsonify({"data": upload})
