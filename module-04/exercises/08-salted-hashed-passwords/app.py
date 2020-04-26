from users import users, find_user
from auth import check_pw

from flask import Flask, request, abort, json
from werkzeug.exceptions import HTTPException


app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    body = request.get_json()
    if body:
        username = body.get('username')
        password = body.get('password')

        if all([username, password]):
            try:
                user = find_user(username)
                check_pw(password, user['password'])
                return {'succes': True}, 201
            except:
                abort(401)
        else:
            abort(400)
    else:
        abort(400)


@app.errorhandler(HTTPException)
def handle_exception(e):
    '''Return JSON instead of HTML for HTTP errors.'''
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        'code': e.code,
        'name': e.name,
        'description': e.description,
    })
    response.content_type = 'application/json'
    return response
