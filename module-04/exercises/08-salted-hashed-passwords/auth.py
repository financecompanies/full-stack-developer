import bcrypt


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def check_pw(password, hashed):
    if not bcrypt.checkpw(password.encode(), hashed):
        raise AuthError(
            {
                'code': 'wrong_credentials',
                'description': 'Wrong credentials.'
            },
            401
        )
