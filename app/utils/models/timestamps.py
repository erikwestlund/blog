from datetime import datetime

import timeago
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func

from app import db


class TimestampMixin(object):
    @declared_attr
    def created_at(cls):
        return db.Column(db.DateTime, server_default=func.now())

    @property
    def created_at_ago(self):
        return timeago.format(self.created_at, datetime.now())

    @declared_attr
    def updated_at(cls):
        return db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    @property
    def updated_at_ago(self):
        return timeago.format(self.updated_at, datetime.now())
