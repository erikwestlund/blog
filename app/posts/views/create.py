from flask import render_template, flash, jsonify
from flask.views import MethodView
from flask_login import login_required

from posts.forms.save_post import SavePostForm


class CreatePost(MethodView):

    @login_required
    def get(self):
       return render_template('posts/create_post.html')

    def post(self):
        form = SavePostForm()
        if form.validate_on_submit():
            flash('Post saved.')
            return jsonify({'success': True})
        else:
            return jsonify(errors=form.errors), 422
