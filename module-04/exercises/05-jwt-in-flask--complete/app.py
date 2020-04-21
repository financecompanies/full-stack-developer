import json
from functools import wraps

from flask import Flask, request, abort
from jose import jwt, exceptions
from urllib.request import urlopen


app = Flask(__name__)

AUTH0_DOMAIN = 'fsnd-auth2.auth0.com'
ALGORITHM = 'RS256'
API_AUDIENCE = 'image'

# Auth0 authorize login flow
# https://fsnd-auth2.auth0.com/authorize?audience=image&response_type=token&client_id=wf608uGgNIHRGCSHqivJp3QKOYsJoPYN&redirect_uri=http://localhost:8080/login-results&state=STATE

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

def verify_decode_jwt(token):
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())

    try:
        unverified_header = jwt.get_unverified_header(token)

        if 'kid' not in unverified_header:
            raise exceptions.JWTError
    except:
        raise AuthError(
            {
                'code': 'invalid_header',
                'description': 'Authorization malformed.'
            }
        , 401)

    rsa_key = {}
    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e'],
            }

    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHM,
                audience=API_AUDIENCE,
                issuer=f'https://{AUTH0_DOMAIN}/'
            )

            return payload
        except exceptions.ExpiredSignatureError:
            raise AuthError(
                {
                    'code': 'token_expired',
                    'description': 'Token expired.'
                }
            , 401)
        except exceptions.JWTClaimsError:
            raise AuthError(
                {
                    'code': 'invalid_claims',
                    'description': 'Incorrect claims. Please, check the audience and issuer.'
                }
            , 401)
        except exceptions.JWTError:
            raise AuthError(
                {
                    'code': 'invalid_signatur',
                    'description': 'Incorrect signature.'
                }
            , 401)
        except Exception:
            raise AuthError(
                {
                    'code': 'invalid_header',
                    'description': 'Unable to parse authentication token.'
                }
            , 400)

    raise AuthError(
        {
            'code': 'invalid_header',
            'description': 'Unable to find the appropriate key.'
        }
    , 400)

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
        try:
            payload = verify_decode_jwt(jwt)
            return f(payload, *args, **kwargs)
        except AuthError as authError:
            abort(authError.status_code)
    return wrapper

@app.route('/headers')
@requires_auth
def headers(payload):
    print(json.dumps(payload, indent=4))
    return f'You\'re correct. You sent to us a valid token!'
