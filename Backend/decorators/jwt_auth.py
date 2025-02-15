import jwt
import datetime
import os
from functools import wraps
from flask import request, jsonify

SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

def generate_token(username):
    # Create a token with a payload that includes the username and an expiration time
    payload = {
        'user': username,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)  # Token expires in 1 hour
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # Expect the token in the Authorization header in the format "Bearer <token>"
        auth_header = request.headers.get('Authorization')
        if auth_header:
            parts = auth_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            # Decode the token to retrieve the payload
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = payload['user']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated