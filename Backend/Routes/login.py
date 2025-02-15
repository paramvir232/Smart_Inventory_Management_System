from flask import Blueprint, request, jsonify
from utils import generate_token

auth_bp = Blueprint('auth',__name__)



@auth_bp.route('/')
def login():
    return f"<h1>{generate_token("hi")}</h1>"