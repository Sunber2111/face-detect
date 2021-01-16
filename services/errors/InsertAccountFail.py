from werkzeug.exceptions import HTTPException

class InsertAccountFail(HTTPException):
    code = 400
    description = 'Thêm Tài Khoản Thất Bại!'
    name = 'Registry Error'
