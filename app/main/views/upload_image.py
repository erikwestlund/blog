from io import BytesIO

from flask import jsonify
from flask.views import MethodView

from app import db
from main.models.image import Image
from utils.uploads import upload_file
from PIL import Image as PillowImage

class UploadImageFile(MethodView):
    def post(self):
        upload = upload_file(upload_type="image")

        if upload["status"] == "error":
            return jsonify({"data": upload}), 422

        uploaded_image = PillowImage.open(upload["data"]["file"])

        image = Image(
            provider=upload["data"]["provider"],
            bucket=upload["data"]["bucket"],
            path=upload["data"]["path"],
            width=uploaded_image.size[0],
            height=uploaded_image.size[1]
        )
        db.session.add(image)
        db.session.commit()

        return jsonify(
            {"data": {"filename": upload["data"]["original_filename"], "image": image}}
        )
