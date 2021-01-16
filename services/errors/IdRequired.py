from werkzeug.exceptions import HTTPException

class IdRequired(HTTPException):
    code = 400
    description = 'Phải có id'
    name = 'Database Error'
