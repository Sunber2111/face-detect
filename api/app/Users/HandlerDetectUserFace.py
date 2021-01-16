from services.errors.NotMatchError import NotMatchError
from services.ai.mapper import map_index_to_id
from bson.objectid import ObjectId 
from services.repositories.Repobase import get_by_id
from infrastructure.security.JwtGennerate import create_token
from services.collections.CollectionsName import AccountColection,UserCollection
from extension import model_predict

def detect(image, acc_id):
    index_predict = model_predict.detect(image,acc_id)
    acc_detect = get_by_id(AccountColection,acc_id)
    user_detect = get_by_id(UserCollection,str(acc_detect['user']))
    if index_predict == 1:
        return {
            'token':create_token(str(user_detect['_id'])),
            'name':user_detect['fullName'],
            'image':user_detect['image']
        }
    raise NotMatchError()

def detect_test(image):
    index_predict = model_predict.detect_test(image)
    return index_predict