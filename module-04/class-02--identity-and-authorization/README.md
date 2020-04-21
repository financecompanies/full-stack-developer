# Identity and Authorization

## [1. Lesson Intro](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/0f6a882a-aff8-474a-b0ec-15a28f8c0c95/concepts/1b5e14f4-daa3-4850-aa9d-f89f79062bae)

### Who are you?

[![](https://img.youtube.com/vi/X3a7uGXxhTM/0.jpg)](https://youtu.be/X3a7uGXxhTM)

### Authentication in the Digital World

[![](https://img.youtube.com/vi/Y1X9yupVhG8/0.jpg)](https://youtu.be/Y1X9yupVhG8)

## [2. Common Authentication Methods](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/0f6a882a-aff8-474a-b0ec-15a28f8c0c95/concepts/84762640-4deb-4aed-8ab2-76adadf68eed)

### Username and Passwords

Most common in the age of SaaS

[![](https://img.youtube.com/vi/Ccm4wie8qlA/0.jpg)](https://youtu.be/Ccm4wie8qlA)

### HTTP Status Codes

Two status codes which are important throughout this course are:

- 401 Unauthorized

    The client must pass authentication before access to this resource is granted. The server cannot validate the identity of the requested party.

- 403 Forbidden

    The client does not have permission to access the resource. Unlike 401, the server knows who is making the request, but that requesting party has no authorization to access the resource.

### Brief Intro to Problems with Passwords

[![](https://img.youtube.com/vi/i2PQhJpb_OI/0.jpg)](https://youtu.be/i2PQhJpb_OI)

Many issues come from user behavior that we cannot directly influence, such as:

- Users forget their passwords
- Users use simple passwords
- Users use common passwords
- Users repeat passwords
- Users share passwords

In contrast, some issues are within **our control** as developers:

- Passwords can be compromised
- Developers can incorrectly check
- Developers can cut corners

### Links about NIST bad passwords and recommendations
- [Easy Ways to Build a Better P@$5w0rd](https://www.nist.gov/blogs/taking-measure/easy-ways-build-better-p5w0rd)
- [Bad passwords and the NIST guidelines](https://rstudio-pubs-static.s3.amazonaws.com/346197_6d0dd053d1b3471c82f733849f0e0d5d.html)
- [1000-most-common-passwords.txt](https://github.com/DavidWittman/wpxmlrpcbrute/blob/master/wordlists/1000-most-common-passwords.txt)
- [NIST Bad Passwords](https://cry.github.io/nbp/)

## [3. Alternative Authentication Methods](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/0f6a882a-aff8-474a-b0ec-15a28f8c0c95/concepts/84762640-4deb-4aed-8ab2-76adadf68eed)

### Single Sign-On (SSO)

[![](https://img.youtube.com/vi/BYSKdCi7hUg/0.jpg)](https://youtu.be/BYSKdCi7hUg)

### Multi-Factor Authentication

[![](https://img.youtube.com/vi/LbbOQBZgRlU/0.jpg)](https://youtu.be/LbbOQBZgRlU)

### Passwordless

[![](https://img.youtube.com/vi/OCSFMzd6SX0/0.jpg)](https://youtu.be/OCSFMzd6SX0)

### Biometric Authentication

[![](https://img.youtube.com/vi/gSm18eliZ1E/0.jpg)](https://youtu.be/gSm18eliZ1E)

### A Friendly Reminder of Risk

[![](https://img.youtube.com/vi/4ZkB1OKkczw/0.jpg)](https://youtu.be/4ZkB1OKkczw)

### Additional Readings:
- [Oath2](https://oauth.net/2/)
- [Auth0 Identity Providers](https://auth0.com/docs/identityproviders)
- [Google Identity Platform](https://developers.google.com/identity/)
- [Magic Links](https://hackernoon.com/magic-links-d680d410f8f7)
- [iOS Biometrics](https://developer.apple.com/documentation/localauthentication)
- [Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en_US)
- [Dance Dance Authentication](https://www.youtube.com/watch?v=VgC4b9K-gYU&feature=youtu.be)

## [4. Third-Party Auth Systems](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/0f6a882a-aff8-474a-b0ec-15a28f8c0c95/concepts/319fa1ba-3d71-459e-870a-c5b601cdce23)

### Why Delegate the Responsibility?

[![](https://img.youtube.com/vi/BBkQ_9SSa88/0.jpg)](https://youtu.be/BBkQ_9SSa88)

### Common Auth Services:
- [Auth0](https://auth0.com/) (We'll be using this throughout the course!)
- [AWS Cognito](https://auth0.com/)
- [Firebase Auth](https://firebase.google.com/docs/auth)
- [Okta](https://www.okta.com/)

## [5. Implementing Auth0](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/0f6a882a-aff8-474a-b0ec-15a28f8c0c95/concepts/4bdfc24c-e822-42fe-994f-052de526036b)

### Working with Auth0
Follow along with the set up at [Auth0.com](auth0.com)!

[![](https://img.youtube.com/vi/Mikr9g_JBaE/0.jpg)](https://youtu.be/Mikr9g_JBaE)

### Using the Auth0 Authorization Code Flow with Hosted Login Pages

[![](https://img.youtube.com/vi/_Fb0HKn0U2I/0.jpg)](https://youtu.be/_Fb0HKn0U2I)

### Auth0 Authorize Link

1. Access [documentation](https://auth0.com/docs/api/authentication?http#authorization-code-flow) and get the authorize URL
2. Replace with your own settings
3. Copy and paste to your browse and then navegate to it
4. Access https://jwt.io/#encoded-jwt to decode the JWT

Final Authorization Code Flow URL

```curl
https://fsnd-auth2.auth0.com/authorize?audience=image&response_type=token&client_id=wf608uGgNIHRGCSHqivJp3QKOYsJoPYN&redirect_uri=http://localhost:8080/login-results&state=STATE
```

## [6. JWT - JSON Web Tokens](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/0f6a882a-aff8-474a-b0ec-15a28f8c0c95/concepts/846d6ed1-148b-41c2-b0fc-364cb1fb938a)

[![](https://img.youtube.com/vi/6TWWT1W_4D4/0.jpg)](https://youtu.be/6TWWT1W_4D4)

## [7. JWT - Datastructure](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/0f6a882a-aff8-474a-b0ec-15a28f8c0c95/concepts/e9a02c51-50d9-4b84-9aeb-3cac33d30b6e)

### Including Data in Our JWT Payload

[![](https://img.youtube.com/vi/rz7saqU8d8Q/0.jpg)](https://youtu.be/rz7saqU8d8Q)

### Parts of a JSON Web Token

[![](https://img.youtube.com/vi/WRYsLYuvgoc/0.jpg)](https://youtu.be/WRYsLYuvgoc)

## [8. JWT - Validation](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/0f6a882a-aff8-474a-b0ec-15a28f8c0c95/concepts/d2353499-1bd9-4e3d-bc11-0156561d30cb)

### Validating JWT Authenticity

[![](https://img.youtube.com/vi/SoT_ETc35vs/0.jpg)](https://youtu.be/SoT_ETc35vs)

If the signature strings match, we can trust that the data within the JWT is authentic.

Additional Resources:
- [JWT.io](https://jwt.io/introduction/) a useful guide and list of popular JSON Web Token implementations.
- [Base64 Encoding](https://en.wikipedia.org/wiki/Base64)
- [HMAC](https://en.wikipedia.org/wiki/HMAC) keyed-hash message authentication code

## [9. Practice - Generating and Verifying JWTs](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/0f6a882a-aff8-474a-b0ec-15a28f8c0c95/concepts/a0f32909-f902-44e7-bd30-ab011e14ed6b)

### Practice - Generating and Verifying JWTs

[Jupyter Notebook](https://r848940c858541xJUPYTERqdhs1cm1.udacity-student-workspaces.com/notebooks/JWT.ipynb)

Result code
```python
import jwt
# We don't need base64 here, we're just demonstrating using it
import base64

# our data that says WHO is making the request
payload = {"user": "john", "name": "John Doe"}

# the HMAC + SHA 256 algorigthm
algo = "HS256"

# this 'string' secret is your public key that validades the identity
secret = "secrecy"

encoded_jwt = jwt.encode(payload, secret, algorithm=algo)
print(encoded_jwt)

decoded_jwt = jwt.decode(payload, secret, verify=True)
print(decoded_jwt)

# here we just demonstrate decoding using base64, we don't need this
# this to encode or decode the jwtp
decoded_base64 = base64.b64decode(str(encoded_jwt).split(".")[1]+"==")
print(decoded_base64)
```

## [10. Practice - Validating Auth0 Tokens](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/0f6a882a-aff8-474a-b0ec-15a28f8c0c95/concepts/87007dfe-8503-40ae-bc21-3ef608c1f45f)

### Practice - Validating Auth0 Tokens

[Jupyter Notebook](https://r848940c858541xJUPYTERqdhs1cm1.udacity-student-workspaces.com/notebooks/Auth0.ipynb)

Result code
```python
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
            break

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
                    "code": "invalid_signature",
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
```

## [11. Recap - Local Storage](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/0f6a882a-aff8-474a-b0ec-15a28f8c0c95/concepts/215e03f8-4d18-44b0-9d02-b80f60c776ae)

### Storing Tokens in Web Browsers

#### Using Local Storage
[Local Storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) is an implementation of a [key-value](https://en.wikipedia.org/wiki/Key-value_database) store which is accessible through a javascript interface in most modern browsers. It is a general purpose interface to store strings which will persist in memory from session to session. It is designed for smaller strings and alternative opensource systems like [localForage](https://github.com/localForage/localForage) exist for large amounts of data.

[![](https://img.youtube.com/vi/uOBGbP8B1yQ/0.jpg)](https://youtu.be/uOBGbP8B1yQ)

## [12. Storing JWTs](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/0f6a882a-aff8-474a-b0ec-15a28f8c0c95/concepts/16ce4887-86aa-4623-b796-5365da02651e)

### Using Javascript to Store JWTs

[![](https://img.youtube.com/vi/WbDEQK3orJ0/0.jpg)](https://youtu.be/WbDEQK3orJ0)

### Security Considerations of Local Storage

[![](https://img.youtube.com/vi/HANOhvWxXTI/0.jpg)](https://youtu.be/HANOhvWxXTI)

### How Cross-Site Scripting Attacks (XSS) are Performed and Mitigated Techniques

[![](https://img.youtube.com/vi/dL-Wc0ZEcIQ/0.jpg)](https://youtu.be/dL-Wc0ZEcIQ)

In this video, we discuss [Input Sanitation](https://wesbos.com/sanitize-html-es6-template-strings/). To clarify this concept, imagine a user submits HTML as part of their name in a form. When you later pull this information from your database and insert it into the HTML template for the website, the browser engine will [render](https://en.wikipedia.org/wiki/Browser_engine) this text on the page. However, if the text contains HTML like `<b>Gabe</b>` this would be interpreted in the browser as HTML and render as **Gabe**. This becomes a problem if malicious code, such as javascript, is saved in place of a valid string. In other words, this malicious text will be interpreted by the browser as code and executed on the client. [Input Sanitation](https://wesbos.com/sanitize-html-es6-template-strings/) transforms characters like `<` to `**&lt;**` which will not be interpreted as code and print as text (<). This step should always be performed on the server to prevent someone from sending the malicious text directly to your server using [curl](https://curl.haxx.se/) or [Postman](https://www.getpostman.com/).

We also mentioned [NPM or Node Package Manager](https://www.npmjs.com/) this is an online database of publicly submitted libraries you can use in your javascript projects. Other public databases of code libraries such as [PIP for Python](https://pypi.org/project/pip/) or [Brew for Mac](https://brew.sh/). Some care should be taken to ensure that these packages are compliant with your license and security policies and are monitored for security vulnerabilities.

### Additional Reading

- Google Chrome Storage documentation
- MDN Web Docs LocalStorage Documentation

### Security Considerations of Local Storage

- Why Cookies Aren't Necessarily Safer
- OWASP XSS Cheat Sheet
- Using Refresh Tokens with Auth0
- HTTP Only Cookies
- Getting Cookies in Flask

### Alternatives to LocalStorage

- localForage javascript library capable of more complex storage tasks.
- HttpOnly Cookies so javascript can't access the token at all.

## [13. Sending Tokens](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/0f6a882a-aff8-474a-b0ec-15a28f8c0c95/concepts/43f64499-9215-45eb-84c1-22a797d2dbbc)

### Accessing Authorization Headers in Flask

[![](https://img.youtube.com/vi/kbBdD73lYTE/0.jpg)](https://youtu.be/kbBdD73lYTE)

### Validating Auth Header Formats and Defining our Decorator

[![](https://img.youtube.com/vi/v8DW_PdE48I/0.jpg)](https://youtu.be/v8DW_PdE48I)

### Sending Tokens from Popular Frontend Frameworks

- [React + Redux - JWT Tutorial](https://jasonwatmore.com/post/2017/12/07/react-redux-jwt-authentication-tutorial-example) There are many ways to include JWTs in requests from frontend frameworks. Jason Watmore has many tutorials for your frontend flavor of choice.
- [Angular Interceptors for Authorization Headers](https://medium.com/@ryanchenkie_40935/angular-authentication-using-the-http-client-and-http-interceptors-2f9d1540eb8)

### Additional Reading

- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) Authorization Header Documentation.
- [Postman Authorization](https://learning.getpostman.com/docs/postman/sending_api_requests/authorization/) Including authorization headers in postman requests.

## [XX. ]()

### SECTION

[![](https://img.youtube.com/vi/VIDEO/0.jpg)](https://youtu.be/VIDEO)

## [XX. ]()

### SECTION

[![](https://img.youtube.com/vi/VIDEO/0.jpg)](https://youtu.be/VIDEO)

## [XX. ]()

### SECTION

[![](https://img.youtube.com/vi/VIDEO/0.jpg)](https://youtu.be/VIDEO)

## [XX. ]()

### SECTION

[![](https://img.youtube.com/vi/VIDEO/0.jpg)](https://youtu.be/VIDEO)

## [XX. ]()

### SECTION

[![](https://img.youtube.com/vi/VIDEO/0.jpg)](https://youtu.be/VIDEO)

## [XX. ]()

### SECTION

[![](https://img.youtube.com/vi/VIDEO/0.jpg)](https://youtu.be/VIDEO)
