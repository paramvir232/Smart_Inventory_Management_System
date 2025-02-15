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
from Routes import blueprints as bp
from config import config

app = Flask(__name__)
app.config.from_object(config)
api = Api(app)
CORS(app)


db = SQLAlchemy(app)

app.register_blueprint(bp[0], url_prefix='/auth')

@app.route('/')
def start():
    return "<h1>START</h1>"

if __name__ == '__main__':
    app.run(debug=True)