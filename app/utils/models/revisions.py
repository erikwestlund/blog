from datetime import datetime

import timeago
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func

from app import db


class RevisionsMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    revision = db.Column(db.JSON)
