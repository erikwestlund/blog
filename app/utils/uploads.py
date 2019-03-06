import os
import time
import uuid
from datetime import datetime

from flask import request, current_app
from werkzeug.utils import secure_filename

from utils.uploads_b2 import upload_to_b2
from utils.uploads_local import upload_to_local
from utils.uploads_s3 import upload_to_s3


def allowed_file(filename, upload_type=None):
    if upload_type == "image":
        allowed_extensions = "pdf,png,jpg,jpeg,gif"
    else:
        allowed_extensions = current_app.config["UPLOAD_ALLOWED_EXTENSIONS"]

    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed_extensions


def upload_file(upload_type=None):

    file_storage_provider = current_app.config["FILE_STORAGE_PROVIDER"]
    upload_dir = get_upload_dir()

    if "file" not in request.files:
        return {"status": "error", "message": "Upload is empty."}

    file = request.files["file"]

    if file.filename == "":
        return {"status": "error", "message": "Upload is empty."}

    if not allowed_file(file.filename, upload_type):
        return {"status": "error", "message": "File type not allowed."}

    if file:
        filename = get_file_name(file)
        path = os.path.join(upload_dir, filename)

        if file_storage_provider == "b2":
            bucket, path_to_file = upload_to_b2(path, file)
        elif file_storage_provider == "s3":
            bucket, path_to_file = upload_to_s3(path, file)
        else:
            bucket, path_to_file = upload_to_local(upload_dir, path, file)

        return {
            "status": "success",
            "data": {
                "file": file,
                "original_filename": file.filename,
                "saved_filename": filename,
                "provider": file_storage_provider,
                "bucket": bucket,
                "path": path_to_file,
            },
        }


def get_upload_dir():
    upload_dir = "%s/%s" % (
        current_app.config["UPLOAD_DIR"],
        datetime.now().strftime("%Y/%m"),
    )
    return upload_dir


def get_file_name(file):
    filename = "%s-%s-%s" % (
        int(time.time()),
        str(uuid.uuid4())[:4],
        secure_filename(file.filename),
    )
    return filename
