import os
from datetime import datetime
from urllib.parse import urlparse

from flask import request, jsonify, current_app
from flask.views import MethodView
from werkzeug.utils import secure_filename

from utils.uploads import allowed_file, upload_to_b2


class UploadFile(MethodView):
    def post(self):
        cloud_provider = current_app.config["CLOUD_FILE_PROVIDER"]
        upload_dir = "%s/%s" % (current_app.config["UPLOAD_DIR"], datetime.now().strftime("%Y/%m"))

        if 'file' not in request.files:
            return jsonify({
                "status": "error",
                "message": "No file sent."
            }), 422

        file = request.files['file']

        if file.filename == '':
            return jsonify({
                "status": "error",
                "message": "File empty."
            }), 422

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            if cloud_provider == "b2":
                path = os.path.join(upload_dir, filename)

                file = upload_to_b2(path, file)

                url = self.get_b2_url_from_file(file)
            else:
                # if no cloud provider, save locally in the static directory
                upload_dir = "static/" + upload_dir
                path = os.path.join(upload_dir, filename)

                if not os.path.exists(upload_dir):
                    os.makedirs(upload_dir)

                file.save(path)

                url = "/" + path

            return jsonify({"data": {
                "path": path,
                "url": url
            }})

    def get_b2_url_from_file(self, file):
        bucket = current_app.config["B2_BUCKET"]
        parsed_url = urlparse(file.connector.download_url)
        url = "%s://%s/file/%s/%s" % (parsed_url.scheme, parsed_url.netloc, bucket, file.file_name)

        return url

