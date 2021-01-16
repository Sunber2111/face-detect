from services.repositories.Repobase import get_all
from services.collections.CollectionsName import UserCollection

def get_all_users_handler():
    return get_all(UserCollection)