from werkzeug.exceptions import HTTPException

class ServerError(HTTPException):
    code = 500
    description = 'An Error Occur When Server Running'
    name = 'Server Error'