import os
from datetime import datetime
from urllib.parse import urlparse

from flask import request, jsonify, current_app, url_for
from flask.views import MethodView
from werkzeug.utils import secure_filename

from app import db
from main.models.image import Image
from utils.uploads import allowed_file, upload_to_b2


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


def upload_file():
    cloud_provider = current_app.config["CLOUD_FILE_PROVIDER"]
    upload_dir = "%s/%s" % (
        current_app.config["UPLOAD_DIR"],
        datetime.now().strftime("%Y/%m"),
    )

    if "file" not in request.files:
        return {"status": "error", "message": "No file sent."}

    file = request.files["file"]

    if file.filename == "":
        return {"status": "error", "message": "File empty."}

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        if cloud_provider == "b2":
            path = os.path.join(upload_dir, filename)

            uploaded_file = upload_to_b2(path, file)

            url = get_b2_url_from_file(uploaded_file)
        else:
            # if no cloud provider, save locally in the static directory
            upload_dir = "static/" + upload_dir
            path = os.path.join(upload_dir, filename)

            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)

            file.save(path)

            url = url_for("main.index") + path

        return {
            "status": "success",
            "data": {
                "original_filename": file.filename,
                "secure_filename": filename,
                "path": path,
                "url": url,
            },
        }


def get_b2_url_from_file(file):
    bucket = current_app.config["B2_BUCKET"]
    parsed_url = urlparse(file.connector.download_url)
    url = "%s://%s/file/%s/%s" % (
        parsed_url.scheme,
        parsed_url.netloc,
        bucket,
        file.file_name,
    )

    return url
