from extension import mongo
from services.errors.DbError import DbError
from services.collections.CollectionsName import AccountColection,UserCollection
from services.errors.LoginFailError import LoginFailError
from services.errors.NotActivateAccount import NotActivateAccount

def login(nameLogin, password):
    result = mongo.db.get_collection(AccountColection).find_one(
        {"namelogin": nameLogin, "password": password})
    if result is None:
        raise LoginFailError()
    if result['isActivate'] == False:
        raise NotActivateAccount()
    return result
