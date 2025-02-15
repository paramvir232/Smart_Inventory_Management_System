from flask import Blueprint, request, jsonify
from Backend.decorators.jwt_auth import generate_token

auth_bp = Blueprint('auth',__name__)



@auth_bp.route('/')
def login():
    return f"<h1>{generate_token("prince")}</h1>"