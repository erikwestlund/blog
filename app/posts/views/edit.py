from flask import render_template, jsonify
from flask.views import MethodView
from flask_login import login_required, current_user

from sqlalchemy import func

from app import db
from main.models.tag import Tag
from posts.forms.save_post import SavePostForm
from posts.models.post import Post, PostRevision
from flask import abort

class EditPost(MethodView):

    @login_required
    def get(self):
        return render_template('posts/edit_post.html')

    @login_required
    def patch(self, post_id):
        post = Post.query.get(post_id)

        if not current_user.has_role('administrator') or current_user.id != post.user_id:
            abort(403)

        form = SavePostForm()

        if form.validate_on_submit():
            revision = PostRevision(post_id=post_id,
                                    revision=post.to_json())
            db.session.add(revision)

            if form.published_at.data and not post.published_at:
                post.published_at = func.now()


            post.title = form.title.data
            post.body = form.body.data
            post.tags = Tag.query.filter(Tag.id.in_(form.tags.data)).all()

            db.session.commit()

            return jsonify({
                'action': 'edit',
                'success': True,
                'post': post
            })
        else:
            return jsonify(errors=form.errors), 422

