from b2blaze import B2
from flask import current_app


def upload_to_b2(path, file, bucket_name=None):
    bucket = get_connected_bucket(bucket_name)

    bucket.files.upload(contents=file.read(), file_name=path)

    return current_app.config["B2_BUCKET"], path


def get_connected_bucket(bucket_name=None):
    return B2().buckets.get(bucket_name or current_app.config["B2_BUCKET"])


def delete_from_b2(path, bucket_name=None):
    bucket = get_connected_bucket(bucket_name)

    file = bucket.files.get(file_name=path)

    file.delete()





