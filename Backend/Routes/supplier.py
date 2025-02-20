from flask import Blueprint, request, jsonify
from Database import CRUD,Product,Supplier
from flask_restful import Resource
from utils import generate_token,token_required

supplier_bp = Blueprint('supplier',__name__)

@supplier_bp.route('/detail')
def detail():
    data = CRUD.universal_query(Supplier)
    return jsonify(data)


@supplier_bp.route('/product_detail')
def supplier():
    data = CRUD.universal_query(
    Supplier,
    joins=[(Product, Supplier.supplierProduct == Product.productId)],
    attributes={
        "Supplier": ["supplierId", "supplierName"],
        "Product": ["productName","productId"]
    }
)
    return jsonify(data)
