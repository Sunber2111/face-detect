from api.app.Users.HandlerGetAllUsers import get_all
from services.collections.CollectionsName import UserCollection

map_index_to_id = {}

def initial_mapper():
    users = get_all(UserCollection)
    for user in users:
        map_index_to_id[user['idModelDetect']] = user['_id']
