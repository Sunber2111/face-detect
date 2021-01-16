import os

MONGO_URI = os.environ.get('MONGO_URI')
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
JWT_COOKIE_CSRF_PROTECT = False
JWT_CSRF_CHECK_FORM = True