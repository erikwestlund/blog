from flask_sqlalchemy import BaseQuery as SqlAlchemyBaseQuery


class BaseQuery(SqlAlchemyBaseQuery):
    def get_or(self, ident, default=None):
        return self.get(ident) or default
