import os
from tempfile import SpooledTemporaryFile, NamedTemporaryFile

import boto3
from flask import current_app

def delete_from_s3(path, bucket_name=None):
    s3 = get_boto_client()
    s3.delete_object(Bucket=bucket_name, Key=path)


def upload_to_s3(path, file, bucket_name=None):
    s3 = get_boto_client()
    bucket_name = bucket_name or current_app.config["AWS_S3_BUCKET"]

    # Need to clone the file because boto3 autocloses the file after uploading to s3,
    # preventing further use of the uploaded file.
    file_s3 = SpooledTemporaryFile()
    file_s3.write(file.read())
    file_s3.seek(0)

    s3.upload_fileobj(
        file_s3,
        bucket_name,
        path,
        ExtraArgs={"ACL": "public-read", "ContentType": file.content_type},
    )

    if not file_s3.closed:
        file_s3.close()

    return bucket_name, path


def get_boto_client():
    session = boto3.session.Session()
    s3 = session.client("s3")
    return s3
