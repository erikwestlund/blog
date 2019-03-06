from flask import Blueprint

from main.views.admin import Admin
from main.views.images import Images
from main.views.index import Index
from main.views.tags import Tags
from main.views.upload_file import UploadFile
from main.views.upload_image import UploadImageFile

main = Blueprint("main", __name__, template_folder="templates", static_folder="static")

main.add_url_rule("/", view_func=Index.as_view("index"))
main.add_url_rule("/admin", view_func=Admin.as_view("admin"))

main.add_url_rule("/tags", view_func=Tags.as_view("tags"))

main.add_url_rule("/admin/uploads", view_func=UploadFile.as_view("upload_file"))
main.add_url_rule(
    "/admin/uploads/image", view_func=UploadImageFile.as_view("upload_image_file")
)

main.add_url_rule("/admin/images/<int:image_id>", view_func=Images.as_view("images"))
