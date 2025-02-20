from flask import Blueprint, request, jsonify
from Database import CRUD,Store_Login
from flask_restful import Resource
from utils import generate_token,token_required

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/login',methods = ['POST'])
def login():
    # data = {
    #     'storeId':124,
    #     'storePassword':"hi",
    # }
    data = request.get_json()
    retrived = CRUD.universal_query(Store_Login,attributes={"Store__Login":['storeId','storePassword']})
    if data in retrived:
        token = generate_token(data.get('storeId'))
        return jsonify(token)
    return {'Error':'Wrong Credentials'},404
    # return jsonify(retrived)


@auth_bp.route('/signup',methods = ['POST'])
def send():
    data = request.get_json()
    result = CRUD.add_item(Store_Login,**data)
    return jsonify(result)

@auth_bp.route('/details/<int:storeId>', methods=['GET'])
# @token_required
def details(storeId):
    result = CRUD.universal_query(Store_Login,filters=[storeId == Store_Login.storeId])
    return jsonify(result)

@auth_bp.route('/change_password/<int:storeId>',methods = ['POST'])
def changePassword(storeId):
    """ Send JSON with this format {'storePassword':'NEW_PASSWORD} """
    data = request.get_json()
    result = CRUD.update_item(Store_Login,storeId,**{'storePassword':data.get('storePassword')})
    return jsonify(result)
