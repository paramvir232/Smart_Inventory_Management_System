from flask import Blueprint, request, jsonify
from Database import CRUD,Product,Store_Login,Inventory,Supplier
from flask_restful import Resource
from utils import generate_token,token_required
import cloudinary

inventory_bp = Blueprint('inventory',__name__)

@inventory_bp.route('/<int:storeId>')
def home(storeId):
    data = CRUD.universal_query(
        Inventory,
        filters=[Inventory.storeId == storeId],
        joins=[
            (Supplier, Supplier.supplierId == Inventory.supplierId),  
            (Product, Supplier.supplierProduct == Product.productId)
        ],
        attributes={
            "Supplier": ["supplierName"],
            "Product": ["productName","productStock"]
        }
    )
    
    return jsonify(data)
