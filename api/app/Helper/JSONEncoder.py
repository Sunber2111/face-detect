import json
from bson import ObjectId
from datetime import date, datetime

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
