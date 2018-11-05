from funcy import lpluck_attr


class ModelAccessorMixin(object):

    def pluck(self, key, collection=None):
        if not collection:
            collection = self.query.all()
        return lpluck_attr(key, collection)

    @staticmethod
    def listify(collection):
        return [i.as_dict() for i in collection]

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
