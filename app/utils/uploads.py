from b2blaze import B2
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from flask import current_app


def allowed_file(filename):
    allowed_extensions = current_app.config["UPLOAD_ALLOWED_EXTENSIONS"]

    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed_extensions


def upload_to_b2(path, file):
    key_id = current_app.config["B2_KEY_ID"]
    application_key = current_app.config["B2_APPLICATION_KEY"]
    bucket_name = current_app.config["B2_BUCKET"]

    b2 = B2(key_id=key_id, application_key=application_key)
    bucket = b2.buckets.get(bucket_name)

    new_file = bucket.files.upload(contents=file.read(), file_name=path)

    return new_file


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
