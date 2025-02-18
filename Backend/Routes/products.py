from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from Database import CRUD,Product
from flask_restful import Resource
from utils import generate_token,token_required
from werkzeug.utils import secure_filename
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


@product_bp.route('/')
def form():
    return render_template('form.html')

@product_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400
    
    # Optionally, secure the filename
    filename = secure_filename(file.filename)
    
    # Upload to Cloudinary
    result = cloudinary.uploader.upload(file)
    secure_url = result.get("secure_url")
    
    if secure_url:
        # Optionally, store secure_url in your database, etc.
        return jsonify({'message': 'File uploaded successfully', 'url': secure_url})
    else:
        return jsonify({'error': 'Failed to upload file'}), 500

 
        


    


