from services.errors.InsertAccountFail import InsertAccountFail
from services.repositories.Repobase import insert
from services.collections.CollectionsName import UserCollection, AccountColection
from bson import ObjectId, DBRef
from datetime import datetime
from api.app.Account.DTO.InsertSuccess import InsertSuccess
import bcrypt


def insert_new_account(data):
    try:
        dataUser = data['user']
        year = int(dataUser['birthDay'].split('-')[0])
        month = int(dataUser['birthDay'].split('-')[1])
        day = int(dataUser['birthDay'].split('-')[2])
        dataUser['birthDay'] = datetime(year, month, day)
        userId = insert(UserCollection, dataUser)
        dataAccount = {}
        dataAccount['namelogin'] = data['namelogin']
        dataAccount['password'] = data['password']
        dataAccount['isActivate'] = data['isActivate']
        dataAccount['isSecurity'] = data['isSecurity']
        dataAccount['user'] = ObjectId(userId)
        dataAccount['role'] = ObjectId(data['role'])
        insert(AccountColection, dataAccount)
        return {'status': 'success', 'description': 'Đăng kí thành công'}
    except:
        raise InsertAccountFail()
