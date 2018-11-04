from pluck import pluck

class ModelAccessorMixin(object):

    def pluck(self, key, collection=None):
        if not collection:
            collection = self.query.all()
        return pluck(collection, key)

    @staticmethod
    def listify(collection):
        return [i.as_dict() for i in collection]

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
