from funcy import lpluck_attr
import json
from utils.models.json_encoder import AlchemyEncoder


class ModelAccessorMixin(object):

    def pluck(self, key, collection=None):
        if not collection:
            collection = self.query.all()
        return lpluck_attr(key, collection)

    @staticmethod
    def listify(collection):
        return [i.to_dict() for i in collection]

    @staticmethod
    def jsonify(collection):
        listified = [i.to_dict() for i in collection]
        return json.dumps(listified, cls=AlchemyEncoder)

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
    def paginated_response(paginated, url='/'):
        return json.dumps({
            'current_page': paginated.page,
            'data': paginated.items,
            # from=1
            # last_page=68
            # first_page_url="https://www.letsrun.com/users/banned?page=68"
            # last_page_url="https://www.letsrun.com/users/banned?page=68"
            # next_page_url="https://www.letsrun.com/users/banned?page=2"
            # path="https://www.letsrun.com/users/banned"
            'per_page': paginated.per_page,
            # prev_page_url=null
            # to=25
            'total': paginated.total
        }, cls=AlchemyEncoder)
