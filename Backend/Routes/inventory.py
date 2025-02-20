from flask import Blueprint, request, jsonify
from Database import CRUD,Product,Store_Login,Inventory,Supplier
from flask_restful import Resource
from utils import generate_token,token_required
import cloudinary

inventory_bp = Blueprint('inventory',__name__)

@inventory_bp.route('/')
def home():
    data = CRUD.universal_query(
    Inventory,
    joins=[(Supplier, Supplier.id == Inventory.supplierId),
        (Product,Supplier.supplierProduct == Product.productId)],
    attributes={
        "Inventory":["storeId"],
        "Supplier": ["supplierName"],
        "Product": ["productName"]
    }
)
    return jsonify(data)