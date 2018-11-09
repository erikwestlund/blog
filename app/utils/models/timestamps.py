from sqlalchemy.sql import func

from app import db


class TimestampMixin(object):
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())