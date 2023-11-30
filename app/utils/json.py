import json

from sqlalchemy import Row


class FlaskJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Row):
            print(obj)
            return {}
        return super(FlaskJSONEncoder, self).default(obj)
