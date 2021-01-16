from werkzeug.exceptions import HTTPException

class LoginFailError(HTTPException):
    code = 400
    description = 'Sai Tên Đăng Nhập Hoặc Mật Khẩu'
    name = 'Login Error'