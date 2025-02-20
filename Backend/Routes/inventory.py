from flask import Blueprint, request, jsonify
from Database import CRUD,Product,Store_Login,Inventory
from flask_restful import Resource
from utils import generate_token,token_required
import cloudinary

inventory_bp = Blueprint('inventory',__name__)

@inventory_bp.route('/')
def home():
    return "<h1>inventory</h1>"