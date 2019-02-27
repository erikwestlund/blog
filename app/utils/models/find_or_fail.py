from sqlalchemy.orm import exc
from werkzeug.exceptions import abort


def find_or_fail(model, *criterion):
    try:
        return model.query.filter(*criterion).one()
    except (exc.NoResultFound, exc.MultipleResultsFound):
        abort(404)
