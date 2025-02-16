from flask import Blueprint, request, jsonify
from utils import generate_token
from Database import CRUD,Store_Login


auth_bp = Blueprint('auth',__name__)



@auth_bp.route('/')
def login():
    result = CRUD.universal_query(Store_Login)
    return jsonify(result)