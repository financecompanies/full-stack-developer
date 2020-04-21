from functools import wraps

from flask import Flask, request, abort


app = Flask(__name__)

def get_token_auth_header():
    if 'Authorization' not in request.headers:
        abort(401)

    auth_header = request.headers['Authorization']
    auth_header_splitted = auth_header.split(' ')

    if len(auth_header_splitted) != 2:
        abort(401)

    auth_header_key, auth_header_value = auth_header_splitted

    if auth_header_key.lower() != 'bearer':
        abort(401)

    return auth_header_value

def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        jwt = get_token_auth_header()
        return f(jwt, *args, **kwargs)
    return wrapper

@app.route('/headers')
@requires_auth
def headers(jwt):
    return f'You\'re correct. You sent to us {jwt}!'
