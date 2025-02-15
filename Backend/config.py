import os
from dotenv import load_dotenv
load_dotenv()
class config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = True

print(os.getenv('SECRET_KEY'))