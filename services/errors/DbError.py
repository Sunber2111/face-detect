from werkzeug.exceptions import HTTPException

class DbError(HTTPException):
    code = 410
    description = 'DataBase Error When Query/Command'
    name = 'Database Error'