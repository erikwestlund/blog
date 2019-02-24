from app import db
from posts.models.post import Post, PostRevision
from flask import render_template, flash, jsonify
from flask.views import MethodView
from flask_login import login_required, current_user

from posts.forms.save_post import SavePostForm

from sqlalchemy import func

class CreatePost(MethodView):

    @login_required
    def get(self):
        return render_template('posts/create_post.html')

    def patch(self):
        form = SavePostForm()
        post = Post.query.get(form.post_id.data)

        if form.action.data == 'unpublish':
            post.published_at = None

            db.session.commit()

            return jsonify({
                'action': form.action.data,
                'success': True,
                'post': post
            })
        elif form.validate_on_submit():
            # save revision
            revision = PostRevision(post_id=form.post_id.data,
                                    revision=post.to_json())
            db.session.add(revision)

            # update current post
            if form.action.data == 'publish':
                post.published_at = func.now()

            # append tags!

            post.title = form.title.data
            post.body = form.body.data

            db.session.commit()

            return jsonify({
                'action': form.action.data,
                'success': True,
                'post': post
            })
        else:
            return jsonify(errors=form.errors), 422

    def post(self):
        form = SavePostForm()

        if form.validate_on_submit():
            post = Post(user_id=current_user.id,
                        title=form.title.data,
                        body=form.body.data)

            if form.action.data == 'publish':
                post.published_at = func.now()

            db.session.add(post)
            db.session.commit()

            return jsonify({
                'action': form.action.data,
                'success': True,
                'post': post
            })
        else:
            return jsonify(errors=form.errors), 422

