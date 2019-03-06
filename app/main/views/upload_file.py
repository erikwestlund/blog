from flask import jsonify
from flask.views import MethodView

from utils.uploads import upload_file


class UploadFile(MethodView):
    def post(self):
        upload = upload_file()

        if upload["status"] == "error":
            return jsonify({"data": upload}), 422

        return jsonify({"data": upload})
