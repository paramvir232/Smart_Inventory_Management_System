from flask import Flask, jsonify, request, abort
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask_migrate import Migrate
from sqlalchemy import inspect
from flask_cors import CORS
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://api_1yct_user:YTnRCqigFRXkkjsZLLyQ2UqQfgjJQjG8@dpg-cumuhiggph6c738a6vpg-a.oregon-postgres.render.com/api_1yct'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)