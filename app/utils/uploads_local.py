import os

def delete_from_local(path, bucket_name=None):
    bucket_name = bucket_name or "static"
    os.remove(os.path.join(bucket_name, path))


def upload_to_local(upload_dir, path, file, bucket_name=None):
    bucket_name = bucket_name or "static"
    storage_dir = os.path.join(bucket_name, upload_dir)
    storage_path = os.path.join(bucket_name, path)

    if not os.path.exists(storage_dir):
        os.makedirs(storage_dir)

    file.save(storage_path)

    return bucket_name, path
