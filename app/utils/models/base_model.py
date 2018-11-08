import json

import sqlalchemy as sa
from flask_sqlalchemy import Model
from funcy import lpluck_attr
from sqlalchemy.ext.declarative import declared_attr

from utils.models.json_encoder import AlchemyEncoder


class BaseModel(Model):

    @declared_attr
    def id(cls):
        for base in cls.__mro__[1:-1]:
            if getattr(base, '__table__', None) is not None:
                type = sa.ForeignKey(base.id)
                break
        else:
            type = sa.Integer

        return sa.Column(type, primary_key=True)


    def pluck(self, key, collection=None):
        if not collection:
            collection = self.query.all()
        return lpluck_attr(key, collection)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def to_json(self):
        if hasattr(self, 'visible'):
            safe = {keep: self.to_dict()[keep] for keep in self.visible}
            return json.dumps(safe, cls=AlchemyEncoder)
        else:
            return json.dumps(self.to_dict(), cls=AlchemyEncoder)

    def __json__(self):
        return self.visible

    @staticmethod
    def listify(collection):
        return [i.to_dict() for i in collection]

    @staticmethod
    def jsonify(collection):
        listified = [i.to_dict() for i in collection]
        return json.dumps(listified, cls=AlchemyEncoder)
