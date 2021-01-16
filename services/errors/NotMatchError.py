from werkzeug.exceptions import HTTPException

class NotMatchError(HTTPException):
    code = 400
    description = 'Không xác thực được, Xin vui lòng thử lại'
    name = 'User Error'