# Access and Authorization

## [01. Lesson Intro](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/2baeea23-aa82-4c96-aaf9-670855db2b70/concepts/d15654c1-799b-47ea-8935-5a430f356411)

### What can you do?

[![](https://img.youtube.com/vi/OBxxynGxLfo/0.jpg)](https://youtu.be/OBxxynGxLfo)

### Authorization in the Digital World

[![](https://img.youtube.com/vi/r9k7yL4othg/0.jpg)](https://youtu.be/r9k7yL4othg)

## [02. Role-Permission Based Access](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/2baeea23-aa82-4c96-aaf9-670855db2b70/concepts/af6ab484-acbe-4934-bc3d-ac77a22355ab)

### Defining our Permissions and Roles

[![](https://img.youtube.com/vi/SMYSNbdVIcI/0.jpg)](https://youtu.be/SMYSNbdVIcI)

### Authorization in our Digital Sequence

[![](https://img.youtube.com/vi/qMRhs57fMl8/0.jpg)](https://youtu.be/qMRhs57fMl8)

### Questions

![](./images/concept-2.question-1.png)

### Additional Resources

- [StackExchange](https://softwareengineering.stackexchange.com/questions/299729/role-vs-permission-based-access-control) discussion on RBAC vs PBAC

## [03. Defining Roles in Auth0](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/2baeea23-aa82-4c96-aaf9-670855db2b70/concepts/56851141-a4be-4edc-adbb-7fa718c6d755)

### Adding Role Configurations to our Auth0 Account

[![](https://img.youtube.com/vi/Rj4AAMjynj0/0.jpg)](https://youtu.be/Rj4AAMjynj0)

## [04. Using RBAC in Flask](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/2baeea23-aa82-4c96-aaf9-670855db2b70/concepts/413c0df9-3464-44e9-9d60-390609edc34f)

### Extending our `@requires_auth` Decorator

[![](https://img.youtube.com/vi/oJTIraxK4UQ/0.jpg)](https://youtu.be/oJTIraxK4UQ)

### Basic Flask Auth task

#### Solution

```python
from flask import Flask, request, abort, jsonify
import json
from functools import wraps
from jose import jwt
from urllib.request import urlopen


app = Flask(__name__)

AUTH0_DOMAIN = "fsnd-auth2.auth0.com"
ALGORITHMS = ["RS256"]
API_AUDIENCE = "image"

IMAGES = [
    {
        "_id": "5eab0b4ef6efe40251394112",
        "name": {"first": "Christian", "last": "Kemp"},
        "tags": ["officia", "do", "consequat", "esse", "sit"],
    },
    {
        "_id": "5eab0b4ef1836d138c739075",
        "name": {"first": "Boone", "last": "Witt"},
        "tags": ["elit", "adipisicing", "mollit", "incididunt", "nisi"],
    },
    {
        "_id": "5eab0b4e79c60b5e12a7a911",
        "name": {"first": "Amalia", "last": "Cervantes"},
        "tags": ["aliqua", "sit", "anim", "nisi", "tempor"],
    },
    {
        "_id": "5eab0b4e8db12c00a2502cb2",
        "name": {"first": "Faulkner", "last": "Mays"},
        "tags": ["eu", "ad", "sit", "irure", "nostrud"],
    },
    {
        "_id": "5eab0b4ea5fb8d0987510f26",
        "name": {"first": "Payne", "last": "Pugh"},
        "tags": ["incididunt", "laborum", "occaecat", "sunt", "exercitation"],
    },
    {
        "_id": "5eab0b4e7e60051407cdb666",
        "name": {"first": "Stein", "last": "Grimes"},
        "tags": ["sint", "reprehenderit", "eu", "fugiat", "cillum"],
    },
    {
        "_id": "5eab0b4e9f77a4a0c85a13dd",
        "name": {"first": "Richard", "last": "Duffy"},
        "tags": ["culpa", "consequat", "ea", "sint", "in"],
    },
    {
        "_id": "5eab0b4e389159a45e32eccf",
        "name": {"first": "Eaton", "last": "Cruz"},
        "tags": ["sint", "fugiat", "velit", "consectetur", "sint"],
    },
]


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError(
            {
                "code": "authorization_header_missing",
                "description": "Authorization header is expected.",
            },
            401,
        )

    parts = auth.split()
    if parts[0].lower() != "bearer":
        raise AuthError(
            {
                "code": "invalid_header",
                "description": 'Authorization header must start with "Bearer".',
            },
            401,
        )

    elif len(parts) == 1:
        raise AuthError(
            {"code": "invalid_header", "description": "Token not found."}, 401
        )

    elif len(parts) > 2:
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Authorization header must be bearer token.",
            },
            401,
        )

    token = parts[1]
    return token


def verify_decode_jwt(token):
    jsonurl = urlopen(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    if "kid" not in unverified_header:
        raise AuthError(
            {"code": "invalid_header", "description": "Authorization malformed."}, 401
        )

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
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer="https://" + AUTH0_DOMAIN + "/",
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError(
                {"code": "token_expired", "description": "Token expired."}, 401
            )

        except jwt.JWTClaimsError:
            raise AuthError(
                {
                    "code": "invalid_claims",
                    "description": "Incorrect claims. Please, check the audience and issuer.",
                },
                401,
            )
        except Exception:
            raise AuthError(
                {
                    "code": "invalid_header",
                    "description": "Unable to parse authentication token.",
                },
                400,
            )
    raise AuthError(
        {
            "code": "invalid_header",
            "description": "Unable to find the appropriate key.",
        },
        400,
    )


def check_permissions(permission, payload):
    if "permissions" not in payload:
        raise AuthError(
            {
                "code": "invalid_claims",
                "description": "Permissions not included in JWT."
            },
            400
        )

    if permission not in payload["permissions"]:
        raise AuthError(
            {
                "code": "unauthorized",
                "description": "Permission not found."
            },
            403
        )


def requires_auth(permission=""):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                token = get_token_auth_header()
                payload = verify_decode_jwt(token)
                check_permissions(permission, payload)
            except AuthError as authError:
                abort(authError.status_code)

            return f(payload, *args, **kwargs)

        return wrapper

    return requires_auth_decorator


@app.route("/images")
@requires_auth('get:images')
def get_images(payload):
    return jsonify(list(IMAGES)), 200

```

#### Tokens to test

User filipebzerra@gmail.com with NO PERMISSIONS

    http://localhost:8080/login-results#

    access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Inl0cUpfdjdjbnN4V0Z3YUIybVd1aSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYXV0aDIuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA2MDc3NzQ3OTc0MjA2MzU3MjIyIiwiYXVkIjpbImltYWdlIiwiaHR0cHM6Ly9mc25kLWF1dGgyLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODgyNjczMDksImV4cCI6MTU4ODI3NDUwOSwiYXpwIjoid2Y2MDh1R2dOSUhSR0NTSHFpdkpwM1FLT1lzSm9QWU4iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOltdfQ.gr0KIBgeTispLhH7sHV_hproJFv-aVFJ2qGlnDJN4c2ZPLN1TRJ2uIfFJs18_IXItZwLmgPDLgKwp0pjy9bGBwNcwjpM1hHv-UE8XlFYqlbEdMf4SiaY5rJpvWqyq8fbflxUzqMJnJjK5QoM0mjQHhIRC8hsVtBBGxSyGcoNqYCoOjzWEzgOj8PoIRdSlUdbT2Cu5KceHIlsfqdJKQl92VYyU5Kzl3UzC1erjOPWfzwu3S0gC7rM-VDvSO_VKyZ1qTjs1Hgl1PqbnvKLHs94khXZkWKmjyXtq7JgNDxvG95m5fMKfPr3S9y8sTvMDqkzCfBk0Iy8m88H74z-C7RiZw

    &scope=openid%20profile%20email&expires_in=7200&token_type=Bearer&state=STATE


User filipebzerra@gmail.com  Google account with VIEWER permission

    http://localhost:8080/login-results

    #access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Inl0cUpfdjdjbnN4V0Z3YUIybVd1aSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYXV0aDIuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA2MDc3NzQ3OTc0MjA2MzU3MjIyIiwiYXVkIjpbImltYWdlIiwiaHR0cHM6Ly9mc25kLWF1dGgyLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODgyNjkyNDUsImV4cCI6MTU4ODI3NjQ0NSwiYXpwIjoid2Y2MDh1R2dOSUhSR0NTSHFpdkpwM1FLT1lzSm9QWU4iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsidmlldzppbWFnZXMiXX0.HQXd_Em2_6sBb4BKs6-gUtcJOZnN0qaXJPvH6DIsro6Ly9M14GthkEBwMigbcu4ZtjfUinbkZpFhxlq-K3VEUDnV-XaYpKejT2B4srgbDnQfDfB-LfgiRCUYYmXfxHF3M3n3qsYxYj82F62WTGToAMlMVb-CsT_rNJcKMraZdTZrIfXvwAdSeNsAz23hTvEQb0aZRfR4c7MvaTrSxi4ToH8Y0ADLv_JANFJP_-tvoSYwgWKjvfds2q0nUQlTpraCXTymv6_iinot9yM_hpJqh_ZLSlixUmKM69gC2aVeOue8fWd6K6jD4fTaoYiwvjaians45wY38zrc7btiDDWKng

    &scope=openid%20profile%20email&expires_in=7200&token_type=Bearer&state=g6Fo2SB6YmVyelBuMEhfcm03UE1pRFNyNDNuaTVES3NJNGRHNaN0aWTZIHI2aXFfd1hPNS1HRUtnVmYyMmI4eTlfYlVET210MDY2o2NpZNkgd2Y2MDh1R2dOSUhSR0NTSHFpdkpwM1FLT1lzSm9QWU4


User filipebzerra@gmail.com account GitHub with GETTER permission

    http://localhost:8080/login-results

    #access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Inl0cUpfdjdjbnN4V0Z3YUIybVd1aSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYXV0aDIuYXV0aDAuY29tLyIsInN1YiI6ImdpdGh1YnwxMDA2MDk1IiwiYXVkIjpbImltYWdlIiwiaHR0cHM6Ly9mc25kLWF1dGgyLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODgyNjkzNDksImV4cCI6MTU4ODI3NjU0OSwiYXpwIjoid2Y2MDh1R2dOSUhSR0NTSHFpdkpwM1FLT1lzSm9QWU4iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZ2V0OmltYWdlcyJdfQ.pxZxLUnGnGbMwtwjIBdThXiuJDkyWAyV1PIba3aaXttziXdrxZA9KJ37HIy1-ZG7iP5ttCvKxtMOopThmAUxKAcHVf4KCHPOTa87buA7RRCovk3fcUR46DvjgtI80ADxHWWDOlb7f8HNDrg1IsmG6lkeIaRApaBQ2-oakWvMbuIigi-P2lmann4THuI6MCyDGpHWuZ9qgnRWXolIwLGO1aq_jCPVepi6jUpwbRSsshOrNbc4ya8V9zJqRgLScHuBw3NVRUOaCetD86mnL93peuqt94gqGlGtNOknOZeVhEBsZH_zjcuLRjEGNSEPQjKax5aubuZStoMEg4OLcHcCaA

    &scope=openid%20profile%20email&expires_in=7200&token_type=Bearer&state=g6Fo2SB6YmVyelBuMEhfcm03UE1pRFNyNDNuaTVES3NJNGRHNaN0aWTZIHI2aXFfd1hPNS1HRUtnVmYyMmI4eTlfYlVET210MDY2o2NpZNkgd2Y2MDh1R2dOSUhSR0NTSHFpdkpwM1FLT1lzSm9QWU4

## [05. Restricting Features in Frontend](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/2baeea23-aa82-4c96-aaf9-670855db2b70/concepts/02439724-158d-4bc3-baf0-674ef2b2a81e)

### Decoding JWTs using Javascript and Preventing Render in Ionic

[![](https://img.youtube.com/vi/VpOWuJ1lcSs/0.jpg)](https://youtu.be/VpOWuJ1lcSs)

### Questions

![](./images/concept-5.question-1.png)

![](./images/concept-5.question-2.png)

### Decoding JWTs in Javascript

[![](https://img.youtube.com/vi/zIAfqP7A37E/0.jpg)](https://youtu.be/zIAfqP7A37E)

### Try it yourself!

Answer the question below using the following JWT and Javascript function.

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imp1aWNlcHJvIiwicGVybWlzc2lvbnMiOlsicG9zdDpqdWljZSJdfQ.7m6ukD61G--xjWGIJJNBRwVJkSrnKwfHOU5KrYEvLW8
```

Javascript to decode JWT:

```javascript
function parseJwt (token) {
    // https://stackoverflow.com/questions/38552003/how-to-decode-jwt-token-in-javascript
   var base64Url = token.split('.')[1];
   var base64 = decodeURIComponent(atob(base64Url).split('').map((c)=>{
       return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
   }).join(''));

   return JSON.parse(base64);
};
```

![](./images/concept-5.question-3.png)

### Additional Resources

- [StackOverflow: How to decode jwt token in javascript](https://stackoverflow.com/questions/38552003/how-to-decode-jwt-token-in-javascript)

## [06. Recap](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/2baeea23-aa82-4c96-aaf9-670855db2b70/concepts/04f12f03-b93b-4e66-93f3-0d5450d3cf52)

### Access and Authorization

[![](https://img.youtube.com/vi/-VOoRVilLlw/0.jpg)](https://youtu.be/-VOoRVilLlw)