import jwt
import base64

payload = {"park": "madison square"}
algorithm = "HS256"
secret = "learning"

encoded_jwt = jwt.encode(payload, secret, algorithm=algorithm)
print(f"Token: {encoded_jwt}")

decoded_jwt = jwt.decode(encoded_jwt, secret, verify=True)
print(f"Decoded token: {decoded_jwt}")

print(type(encoded_jwt))
decoded_jwt = base64.b64decode(str(encoded_jwt).split(".")[1]+"==")
print(f'Decoded token {decoded_jwt} with base64')