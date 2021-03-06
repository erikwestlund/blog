import sys
from datetime import datetime


from flask import abort, current_app
from flask import flash
from flask import render_template, jsonify
from flask.views import MethodView
from flask_login import login_required, current_user
from slugify import slugify
from sqlalchemy import func, null as sqlalchemy_null

from app import db
from main.models.image import Image
from main.models.tag import Tag
from posts.forms.save_post import SavePostForm
from posts.models.post import Post, PostRevision
from utils.acl import user_can_write_posts
from utils.models.find_or_fail import find_or_fail


class FetchPost(MethodView):
    @user_can_write_posts
    def get(self, post_id):
        post = Post.query.get(post_id)

        if not post.editable:
            abort(403)

        return jsonify({"data": post.to_dict()})


class EditPost(MethodView):
    @user_can_write_posts
    def get(self, post_id):
        post = find_or_fail(Post, Post.id == post_id)

        if not post.editable:
            abort(403)

        return render_template("posts/edit.html", post_id=post_id, title="Edit Post")

    @user_can_write_posts
    def delete(self, post_id):
        post = find_or_fail(Post, Post.id == post_id)

        if not post.editable:
            abort(403)

        db.session.delete(post)
        db.session.commit()

        flash("Post successfully deleted.")

        return jsonify({"action": "delete", "success": True, "post": post})

    @user_can_write_posts
    def patch(self, post_id):
        post = find_or_fail(Post, Post.id == post_id)

        if not post.editable:
            abort(403)

        form = SavePostForm(post)

        if form.validate_on_submit():
            revision = PostRevision(post_id=post_id, revision=post.to_json())
            db.session.add(revision)

            post.title = form.title.data
            post.body = form.body.data
            post.primary_image_id = form.primary_image_id.data

            if form.published_at.data and not post.published_at:
                post.published_at = datetime.now()
            elif form.published_at.data and post.published_at:
                post.published_at = form.published_at.data
            elif not form.published_at.data and post.published_at:
                post.published_at = None

            if not form.slug.data and post.published_at:
                post.slug = post.generate_slug(form.title.data, form.published_at.data)
            elif form.slug.data:
                post.slug = slugify(form.slug.data)

            post.images = Image.query.filter(
                Image.id.in_(form.uploaded_images.data)
            ).all()
            post.tags = Tag.query.filter(Tag.id.in_(form.tags.data)).all()

            db.session.commit()

            return jsonify(
                {
                    "action": "edit",
                    "success": True,
                    "post": post,
                    "images": form.uploaded_images.data,
                }
            )
        else:
            return jsonify(errors=form.errors), 422
