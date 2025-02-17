from flask import Blueprint, request, jsonify
from utils import generate_token
from Database import CRUD,Store_Login
from flask_restful import Resource
from utils import generate_token

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/login',methods = ['POST'])
def login():
    # data = {
    #     'storeId':124,
    #     'storePassword':"hi",
    # }
    data = request.get_json()
    retrived = CRUD.universal_query(Store_Login,attributes=['storeId','storePassword'])
    if data in retrived:
        token = generate_token(data.get('storeId'))
        return jsonify(token)
    return {'Error':'Wrong Credentials'},404


@auth_bp.route('/signup',methods = ['POST'])
def send():
    data = request.get_json()
    result = CRUD.add_item(Store_Login,**data)
    return jsonify(result)

@auth_bp.route('/details')
def details():
    result = CRUD.get_all_items(Store_Login)
    return jsonify(result)

@auth_bp.route('/change_password')
def changePassword():
    # data = {
    #     'storeId':1,
    #     'storePassword':"Prince",
    # }
    data = request.json()
    result = CRUD.update_item(Store_Login,data.get('storeId'),**{'storePassword':data.get('storePassword')})
    return jsonify(result)
