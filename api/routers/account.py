from flask import Blueprint, request, json
from api.app.Users.HandlerLoginUser import login_handler
from api.app.Account.HandlerAddAccount import insert_new_account
from api.app.Helper.JSONEncoder import JSONEncoder
from api.app.Account.HandlerGetAllAccount import get_all_accounts
from bson import json_util

account = Blueprint('account', __name__)

@account.route('/login', methods=['POST'])
def login():
    return json.dumps(login_handler(request.json), cls=JSONEncoder)

@account.route('/registry', methods=['POST'])
def registry():
    return json.dumps(insert_new_account(request.get_json()), cls=JSONEncoder)

@account.route('/getallaccount', methods=['GET'])
def get_all():
    return json.dumps(get_all_accounts(), cls=JSONEncoder)
