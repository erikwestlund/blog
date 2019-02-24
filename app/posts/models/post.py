from app import db
from utils.models.timestamps import TimestampMixin

tag_post = db.Table('tag_post',
                      db.Column('tag_id', db.Integer(), db.ForeignKey('tag.id')),
                      db.Column('post_id', db.Integer(), db.ForeignKey('post.id')))


class Post(db.Model, TimestampMixin):
    visible = ['id', 'user_id', 'title', 'body', 'published_at', ]

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    title = db.Column(db.String(255), nullable=False, server_default=u'')
    body = db.Column(db.Text(), nullable=False, server_default=u'')
    published_at = db.Column(db.DateTime())

    # Relationships
    tags = db.relationship('Tag', secondary=tag_post,
                            lazy='dynamic',
                            cascade='save-update',
                            backref=db.backref('posts', lazy='dynamic'))

    revisions = db.relationship('PostRevision', backref='post', lazy=True)

    def __repr__(self):
        return f"Post('{self.title}, {self.body}')"


class PostRevision(db.Model, TimestampMixin):
    visible = ['id', 'post_id', 'revision']

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    revision = db.Column(db.JSON)
