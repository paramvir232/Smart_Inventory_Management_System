from flask import Blueprint, request, jsonify
from Database import CRUD,Product,Store_Login,Inventory,Supplier
from flask_restful import Resource
from utils import generate_token,token_required
import cloudinary

product_bp = Blueprint('product',__name__)
secure_url =None

@product_bp.route('/add_product', methods=['POST'])
def add_product():
    try:
        # Get form fields and ensure they're not empty
        product_name = request.form.get('productName')
        product_price = request.form.get('productPrice')
        product_stock = request.form.get('productStock')
        delivered_date = request.form.get('delivered_date')
        next_delivery_date = request.form.get('next_delivery_date')
        product_default_order = request.form.get('productDefaultOrder')
        product_sold = request.form.get('productSold')
        product_status = request.form.get('productStatus')
        product_id = request.form.get('productId')  # Optional: If productId is generated, no need to get it

        if not all([product_name, product_price, product_stock, product_status]):
            return jsonify({"message": "Missing required fields: productName, productPrice, productStock, productStatus"}), 400

        # Handle Image Upload to Cloudinary
        image_url = None
        if 'image' in request.files:
            image = request.files['image']
            upload_result = cloudinary.uploader.upload(image)
            image_url = upload_result.get('secure_url')

        # Convert dates to datetime objects (if present)
        # delivered_date = datetime.strptime(delivered_date, "%Y-%m-%d") if delivered_date else None
        # next_delivery_date = datetime.strptime(next_delivery_date, "%Y-%m-%d") if next_delivery_date else None

        # Prepare data for add_item
        product_data = {
            "productId": product_id,
            "productName": product_name,
            "productPrice": float(product_price),
            "productStock": int(product_stock),
            "delivered_date": delivered_date,
            "next_delivery_date": next_delivery_date,
            "productDefaultOrder": int(product_default_order) if product_default_order else None,
            "productSold": int(product_sold) if product_sold else None,
            "productStatus": product_status,
            "image_url": image_url
        }

        # Call the generic add_item method
        result = CRUD.add_item(Product, **product_data)
        return jsonify(result), 200 if "Inserted" in result.get("message", "") else 500

    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500


# @product_bp.route('/')
# def form():
#     data = CRUD.universal_query(
#     Product,
#     filters=[Product.productId=1],
#     joins=[(Store_Login, Product.productId == Store_Login.storeId)]
# )

#     return jsonify(data)

@product_bp.route('/detail/<int:productId>')
def product_detail(productId):
    data = CRUD.get_item(Product,productId)
    return jsonify(data)

@product_bp.route('/lowstock/<int:storeId>')
def low_stock_products(storeId):
    data = CRUD.universal_query(
        Inventory,
        filters=[Inventory.storeId == storeId, Product.productStock < 10],  # Filter by store and stock < 10
        joins=[
            (Supplier, Supplier.supplierId == Inventory.supplierId),  
            (Product, Supplier.supplierProduct == Product.productId)
        ],
        attributes={
            "Product": ["productName", "productStock"],
            "Supplier": ["supplierName"]
        }
    )

    return jsonify(data)


 
        


    


