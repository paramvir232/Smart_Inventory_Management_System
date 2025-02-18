# models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, DateTime
from datetime import datetime
# from main import db

db = SQLAlchemy()

class Store_Login(db.Model):
    storeId = db.Column(db.Integer, primary_key=True)
    storePassword = db.Column(db.String(80),nullable=False)
    storeName= db.Column(db.String(100), nullable=False)
    storeLocation = db.Column(db.String(100), nullable=False)
    storeContact = db.Column(db.Integer, nullable=False)


    def serialize(self):
        """Serialize Product object to dictionary"""
        return {
            'Store_id': self.storeId,
            'Store_name': self.storeName,
            'Store_Location': self.storeLocation,
            'Store_Contact': self.storeContact

        }


class Product(db.Model):
    productId = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    productPrice = db.Column(db.Float, nullable=False)
    productStock = db.Column(db.Integer, nullable=False)
    delivered_date = db.Column(Date,nullable=True)        
    next_delivery_date = db.Column(Date,nullable=True) 
    productDefaultOrder =  db.Column(db.Integer, nullable=False)
    productSold = db.Column(db.Integer, nullable=False)
    productStatus = db.Column(db.String(20), nullable=False)

    def serialize(self):
        """Return object data in easily serializable format."""
        return {
            "productId": self.productId,
            "productName": self.productName,
            "image_url": self.image_url,
            "productPrice": self.productPrice,
            "productStock": self.productStock,
            "delivered_date": self.delivered_date.isoformat() if self.delivered_date else None,
            "next_delivery_date": self.next_delivery_date.isoformat() if self.next_delivery_date else None,
            "productDefaultOrder": self.productDefaultOrder,
            "productSold": self.productSold,
            "productStatus": self.productStatus,
        }


# class Supplier(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     contact = db.Column(db.String(120), nullable=True)

# class InventoryTransaction(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     transaction_type = db.Column(db.String(50), nullable=False)  # 'IN' or 'OUT'
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow)
#     product = db.relationship('Product', backref=db.backref('transactions', lazy=True))
