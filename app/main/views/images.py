from flask import jsonify
from flask.views import MethodView
from utils.uploads_b2 import delete_from_b2

from app import db
from main.models.image import Image
from utils.models.find_or_fail import find_or_fail
from utils.uploads_local import delete_from_local
from utils.uploads_s3 import delete_from_s3


class Images(MethodView):
    def delete(self, image_id):
        image = find_or_fail(Image, Image.id == image_id)

        if image.provider == "b2":
            delete_from_b2(image.path, image.bucket)
        elif image.provider == "s3":
            delete_from_s3(image.path, image.bucket)
        else:
            delete_from_local(image.path, image.bucket)

        db.session.delete(image)
        db.session.commit()

        return jsonify({"data": {"image": image}})
