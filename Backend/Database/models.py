# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from main import db

db = SQLAlchemy()

class Store_Login(db.Model):
    storeId = db.Column(db.Integer, primary_key=True)
    storePassword = db.Column(db.String(80),nullable=False)
    storeName= db.Column(db.String(100), nullable=False)
    storeLocation = db.Column(db.String(100), nullable=False)
    storeContact = db.Column(db.Integer, nullable=False)


# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     stock = db.Column(db.Integer, nullable=False)

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
