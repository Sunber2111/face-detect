from flask_jwt_extended import create_access_token
import datetime

def create_token(id_user):
    expires = datetime.timedelta(days=1)
    return create_access_token(identity=id_user,expires_delta=expires)
