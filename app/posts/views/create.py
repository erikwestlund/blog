from flask import render_template
from flask.views import MethodView

from flask_login import login_required

class CreatePost(MethodView):

    @login_required
    def get(self):
       return render_template('posts/create_post.html')

    def post(self):
        pass
