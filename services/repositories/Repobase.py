from extension import mongo
from services.errors.DbError import DbError
from services.errors.IdRequired import IdRequired
from bson.objectid import ObjectId

def get_all(collection_name):
    try:
        return [doc for doc in mongo.db.get_collection(collection_name).find({})]
    except NameError:
        raise DbError()


def get_filter(collection_name, object_filter):
    try:
        return [doc for doc in mongo.db.get_collection(collection_name).find(object_filter)]
    except NameError:
        raise DbError()


def get_by_id(collection_name, id):
    try:
        return mongo.db.get_collection(collection_name).find_one({'_id': ObjectId(id)})
    except NameError:
        raise DbError()


def update(collection_name, new_obj):
    try:
        if '_id' not in new_obj:
            raise IdRequired()
        return mongo.db.get_collection(collection_name).find_one_and_update({'_id': ObjectId(new_obj['_id'])}, {"$set": new_obj})
    except:
        raise DbError()


def insert(collection_name, new_obj):
    return mongo.db.get_collection(collection_name).insert(new_obj)
