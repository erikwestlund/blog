from flask import jsonify
from flask.views import MethodView

from posts.forms.preview import PreviewForm
from posts.models.post import Post


class RenderPreview(MethodView):
    def post(self):
        preview = PreviewForm()

        return jsonify({"html": Post.convert_markdown_to_html(preview.body.data)})
