from sqlalchemy.ext.declarative import DeclarativeMeta
from flask import json


class AlchemyEncoder(json.JSONEncoder):
    """From: https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json"""

    def default(self, o):
        if isinstance(o.__class__, DeclarativeMeta):
            data = {}
            fields = o.__json__() if hasattr(o, "__json__") else dir(o)
            for field in [
                f
                for f in fields
                if not f.startswith("_")
                and f not in ["metadata", "query", "query_class"]
            ]:
                value = o.__getattribute__(field)
                try:
                    json.dumps(value)
                    data[field] = value
                except TypeError:
                    data[field] = None
            return data
        return json.JSONEncoder.default(self, o)
