from app import db
from utils.models.timestamps import TimestampMixin

tags_posts = db.Table('tags_posts',
                      db.Column('tag_id', db.Integer(), db.ForeignKey('tag.id')),
                      db.Column('post_id', db.Integer(), db.ForeignKey('post.id')))


class Post(db.Model, TimestampMixin):
    visible = ['id', 'draft_of', 'user_id', 'title', 'body', 'autosave', 'published_at', ]

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    draft_of = db.Column(db.Integer)
    title = db.Column(db.String(255), nullable=False, server_default=u'')
    body = db.Column(db.Text(), nullable=False, server_default=u'')
    auto_save = db.Column(db.Boolean())
    published_at = db.Column(db.DateTime())

    # Relationships
    tags = db.relationship('Tag', secondary=tags_posts,
                            lazy='dynamic',
                            cascade='save-update',
                            backref=db.backref('posts', lazy='dynamic'))

    def __repr__(self):
        return f"Post('{self.title}, {self.body}')"
