from urllib.parse import urlparse

from b2blaze import B2
from flask import current_app


def delete_from_b2(file_name):
    bucket_name = current_app.config["B2_BUCKET"]

    b2 = B2()
    bucket = b2.buckets.get(bucket_name)

    file = bucket.files.get(file_name=file_name)

    file.delete()

    return file


def delete_file(filename):
    cloud_provider = current_app.config["CLOUD_FILE_PROVIDER"]

    if filename == "":
        return {"status": "error", "message": "No file specified."}

    if cloud_provider == "b2":
        pass
    else:
        pass

    return {"status": "error", "message": "File could not be deleted."}

def get_s3_url_from_file(path):
    bucket_url = current_app.config["AWS_S3_BUCKET_URL"]

    return "%s/%s" % (bucket_url, path)

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