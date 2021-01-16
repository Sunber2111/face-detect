from services.repositories.AccountRepo import login
from infrastructure.security.JwtGennerate import create_token

def login_handler(account):
    acc = login(account['namelogin'], account['password'])
    id = str(acc['_id'])
    return {
        'status':'success',
        'isNext':acc['isSecurity'],
        'acc_id': id
    }
