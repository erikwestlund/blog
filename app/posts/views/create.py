from app import db
from posts.models.post import Post
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

        # if action is save but no post id is set, create a post
        # but dont set published_at date or draft_of
        if form.action.data == 'save' and not form.post_id.data:
            post = Post(title=form.title.data,
                        body=form.body.data)
            db.session.add(post)
            db.session.commit()
        else:
            post = {}

        if form.validate_on_submit():
            flash('Post saved.')
            return jsonify({
                'success': True,
                'post': post
            })
        else:
            return jsonify(errors=form.errors), 422
