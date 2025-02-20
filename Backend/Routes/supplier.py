from flask import Blueprint, request, jsonify
from Database import CRUD,Product,Supplier
from flask_restful import Resource
from utils import generate_token,token_required

supplier_bp = Blueprint('supplier',__name__)

@supplier_bp.route('/info')
def detail():
    data = CRUD.universal_query(Supplier, attributes={"Supplier": ["supplierName", "supplierContact", "supplierEmail"]})

    # Remove duplicates using a set for uniqueness
    unique_suppliers = []
    seen = set()

    for supplier in data:
        key = (supplier["supplierName"], supplier["supplierContact"], supplier["supplierEmail"])
        if key not in seen:
            seen.add(key)
            unique_suppliers.append(supplier)

    return jsonify(unique_suppliers)



@supplier_bp.route('/detail')
def supplier():
    data = CRUD.universal_query(
    Supplier,
    joins=[(Product, Supplier.supplierProduct == Product.productId)],
    attributes={
        "Supplier": ["supplierId", "supplierName","supplierContact"],
        "Product": ["productName","productPrice"]
    }
)
    return jsonify(data)
