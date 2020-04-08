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

Additional Resources:
- [JWT.io](https://jwt.io/introduction/) a useful guide and list of popular JSON Web Token implementations.
- [Base64 Encoding](https://en.wikipedia.org/wiki/Base64)
- [HMAC](https://en.wikipedia.org/wiki/HMAC) keyed-hash message authentication code

## [9. Practice - Generating and Verifying JWTs](https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/0f6a882a-aff8-474a-b0ec-15a28f8c0c95/concepts/a0f32909-f902-44e7-bd30-ab011e14ed6b)

### Practice - Generating and Verifying JWTs

[Jupyter Notebook](https://r848940c858541xJUPYTERqdhs1cm1.udacity-student-workspaces.com/notebooks/JWT.ipynb)

Code
```python
import jwt
import base64

payload = {"user": "john", "name": "John Doe"}
algo = "HS256"
secret = "secrecy"

encoded_jwt = jwt.encode(payload, secret, algorithm=algo)
print(encoded_jwt)

decoded_jwt = jwt.decode(payload, secret, verify=True)
print(decoded_jwt)

decoded_base64 = base64.b64decode(str(encoded_jwt).split(".")[1]+"==")
print(decoded_base64)
```

## [XX. ]()

### SECTION

[![](https://img.youtube.com/vi/VIDEO/0.jpg)](https://youtu.be/VIDEO)

## [XX. ]()

### SECTION

[![](https://img.youtube.com/vi/VIDEO/0.jpg)](https://youtu.be/VIDEO)