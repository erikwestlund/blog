import os
import time
import uuid
from datetime import datetime
from urllib.parse import urlparse

import boto3
from b2blaze import B2
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from flask import request, jsonify, current_app, url_for
from flask.views import MethodView
from werkzeug.utils import secure_filename

from app import db
from main.models.image import Image
from utils.files import get_b2_url_from_file, get_s3_url_from_file


def allowed_file(filename):
    allowed_extensions = current_app.config["UPLOAD_ALLOWED_EXTENSIONS"]

    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed_extensions


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
        filename = "%s-%s-%s" % (
            int(time.time()),
            str(uuid.uuid4())[:4],
            secure_filename(file.filename),
        )

        if cloud_provider == "b2":
            path = os.path.join(upload_dir, filename)

            uploaded_file = upload_to_b2(path, file)

            url = get_b2_url_from_file(uploaded_file)
        elif cloud_provider == "s3":
            path = os.path.join(upload_dir, filename)

            uploaded_file = upload_to_s3(path, file)

            url = get_s3_url_from_file(path)

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
                "saved_file": filename,
                "path": path,
                "url": url,
            },
        }
    return {"status": "error", "message": "File could not be uploaded."}


def upload_to_b2(path, file):
    bucket_name = current_app.config["B2_BUCKET"]

    b2 = B2()
    bucket = b2.buckets.get(bucket_name)

    new_file = bucket.files.upload(contents=file.read(), file_name=path)

    return new_file


def upload_to_s3(path, file):
    s3 = boto3.client("s3")
    bucket_name = current_app.config["AWS_S3_BUCKET"]

    s3.upload_fileobj(
        file,
        bucket_name,
        path,
        ExtraArgs={"ACL": "public-read", "ContentType": file.content_type},
    )

    return path


def upload_to_cloudinary(path):
    response = upload(path)

    url, options = cloudinary_url(
        response["public_id"],
        format=response["format"],
        width=200,
        height=150,
        crop="fill",
    )

    return {"url": url, "options": options}
