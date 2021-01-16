from services.repositories.Repobase import get_all,get_by_id
from services.collections.CollectionsName import AccountColection,UserCollection

def get_all_accounts():
    accs = get_all(AccountColection)
    i=0
    for x in accs:
        if x['user'] is not None:
            accs[i]['user'] = get_by_id( UserCollection, accs[i]['user'] )
        if x['role'] is not None:
             accs[i]['role'] = get_by_id( 'roles', accs[i]['role'] )
        i+=1
    return accs
