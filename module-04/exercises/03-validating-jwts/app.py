import json
from jose import jwt
from urllib.request import urlopen


AUTH0_DOMAIN = "fsnd-auth2.auth0.com"
ALGORITHM = "RS256"
API_AUDIENCE = "image"

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

def verify_decode_jwt(token):
    jsonurl = urlopen(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())

    unverified_header = jwt.get_unverified_header(token)

    if "kid" not in unverified_header:
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Authorization malformed."
            }
        , 401)

    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"],
            }

    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHM,
                audience=API_AUDIENCE,
                issuer=f"https://{AUTH0_DOMAIN}/"
            )

            return payload
        except jwt.ExpiredSignatureError:
            raise AuthError(
                {
                    "code": "token_expired",
                    "description": "Token expired."
                }
            , 401)
        except jwt.JWTClaimsError:
            raise AuthError(
                {
                    "code": "invalid_claims",
                    "description": "Incorrect claims. Please, check the audience and issuer."
                }
            , 401)
        except jwt.JWTError:
            raise AuthError(
                {
                    "code": "invalid_signatur",
                    "description": "Incorrect signature."
                }
            , 401)
        except Exception:
            raise AuthError(
                {
                    "code": "invalid_header",
                    "description": "Unable to parse authentication token."
                }
            , 400)

    raise AuthError(
        {
            "code": "invalid_header",
            "description": "Unable to find the appropriate key."
        }
    , 400)


if __name__ == "__main__":
    token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Inl0cUpfdjdjbnN4V0Z3YUIybVd1aSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYXV0aDIuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA2MDc3NzQ3OTc0MjA2MzU3MjIyIiwiYXVkIjpbImltYWdlIiwiaHR0cHM6Ly9mc25kLWF1dGgyLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODcyNTg1NTEsImV4cCI6MTU4NzI2NTc1MSwiYXpwIjoid2Y2MDh1R2dOSUhSR0NTSHFpdkpwM1FLT1lzSm9QWU4iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIn0.NR4iukicF9LEUlSUANVqMXjtM5wKYb5ggv_3Tg53cQdMHiBRf8aa8XgV29l9odbQpQtQ9umtFeZbtGS_VU5aSap-0kvCZ_9qE2o-m8tMfv4JeaDleKiidT0Yxh6hB-ejIYju6xY3remfqo4NnqHlNih_s5NxmbIBu2gDY0oGIOM5sZe393dg3LFeWFqk4mS95Y5GT5UqYgwhxE-fdkJe_63Jqlk1-AuUt8la3du3Fj5H1QjH-hQ7x_4NktUE6tHRXv_TRoe6_xhNK6rfzYvoW67Q7_OcEmXnR-XRQk9A752AyHROXa5bZyWACv4-GFcwV-vMLLvNPSjEfa6cGS0nWA"
    payload = verify_decode_jwt(token)
    print(json.dumps(payload, indent=4))