from werkzeug.exceptions import HTTPException


class NotActivateAccount(HTTPException):
    code = 401
    description = 'Account was not activate. Please Activate !'
    name = 'Login Error'
