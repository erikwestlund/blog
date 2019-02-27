from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError


def first_or_create(
    session, model, create_method="", create_method_kwargs=None, **kwargs
):
    """From: http://skien.cc/blog/2014/01/15/sqlalchemy-and-race-conditions-implementing/"""
    try:
        return session.query(model).filter_by(**kwargs).one()
    except NoResultFound:
        kwargs.update(create_method_kwargs or {})
        created = getattr(model, create_method, model)(**kwargs)
        try:
            session.add(created)
            session.commit()
            return created
        except IntegrityError:
            session.rollback()
            return session.query(model).filter_by(**kwargs).one()
