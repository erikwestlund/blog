from flask_sqlalchemy import BaseQuery as SqlAlchemyBaseQuery



class BaseQuery(SqlAlchemyBaseQuery):
    def get_or(self, ident, default=None):
        return self.get(ident) or default

    def first_or_create(model, **kwargs):
        instance = db.session.query(model).filter_by(**kwargs).first()
        if instance:
            return instance
        else:
            instance = model(**kwargs)
            return instance
