import json


class InvalidateLoginError():

    def __init__(self, errors):
        self.errors = []
        for x in errors:
            self.errors.append(errors[x])

    def toJSON(self):
        return json.dumps(self.__dict__)
