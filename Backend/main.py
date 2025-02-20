from flask import Flask, jsonify, request, abort,render_template
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask_migrate import Migrate
from sqlalchemy import inspect
from flask_cors import CORS
from functools import wraps
from Database import CRUD,Product,Store_Login,Inventory,Supplier
from Routes import blueprints as bp
from config import config
from Database import db
import cloudinary
import os
from dotenv import load_dotenv
from utils import generate_token,token_required

load_dotenv()

cloudinary.config(
  cloud_name = os.getenv('Cloud_name'),
  api_key = os.getenv('API_key'),
  api_secret = os.getenv('API_secret')
)

app = Flask(__name__)
app.config.from_object(config)
# api = Api(app)
CORS(app, supports_credentials=True)
CORS(bp[0], supports_credentials=True)
db.init_app(app)
migrate = Migrate(app, db)


# db = SQLAlchemy(app)

app.register_blueprint(bp[0], url_prefix='/auth')
app.register_blueprint(bp[1], url_prefix='/product')
app.register_blueprint(bp[2], url_prefix='/supplier')
app.register_blueprint(bp[3], url_prefix='/inventory')





@app.route('/')
def start():
    return render_template('form.html')

@app.route('/login',methods = ['POST'])
def login():
    data = request.get_json()
    retrived = CRUD.universal_query(Store_Login,attributes={"Store__Login":['storeId','storePassword']})
    if data in retrived:
        token = generate_token(data.get('storeId'))
        return jsonify({'Token':token})
    return {'Error':'Wrong Credentials'},404

# with app.app_context():
#     db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

# DATABASE_URL = app.config["SQLALCHEMY_DATABASE_URI"]

# print(f"Database URL: {DATABASE_URL}")