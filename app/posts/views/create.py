from datetime import datetime

from flask import render_template, jsonify
from flask.views import MethodView
from flask_login import login_required, current_user
from sqlalchemy import func

from app import db
from main.models.image import Image
from main.models.tag import Tag
from posts.forms.save_post import SavePostForm
from posts.models.post import Post


class CreatePost(MethodView):
    @login_required
    def get(self):
        return render_template("posts/create.html")

    @login_required
    def post(self):
        form = SavePostForm()

        if form.validate_on_submit():
            post = Post(
                user_id=current_user.id, title=form.title.data, body=form.body.data
            )

            if form.published_at.data and not post.published_at:
                post.published_at = datetime.now()

            if post.published_at:
                post.slug = Post.generate_slug(form.title.data, str(post.published_at))

            post.images = Image.query.filter(
                Image.id.in_(form.uploaded_images.data)
            ).all()
            post.tags = Tag.query.filter(Tag.id.in_(form.tags.data)).all()

            db.session.add(post)
            db.session.commit()

            return jsonify({"action": "create", "success": True, "post": post})
        else:
            return jsonify(errors=form.errors), 422
