from cryptography.fernet import Fernet


FERNET = None

def generate_key():
    return Fernet.generate_key()

def init_fernet(key):
    global FERNET
    if FERNET is None:
        FERNET = Fernet(key)

def encrypt(key, message):
    init_fernet(key)
    print(f'Fernet key: {key}')

    token = FERNET.encrypt(message)
    return token

def decrypt(key, message):
    init_fernet(key)
    print(f'Fernet key: {key}')

    original = FERNET.decrypt(message)
    return original

if __name__ == "__main__":
    key=b'8cozhW9kSi5poZ6TWFuMCV123zg-9NORTs3gJq_J5Do='
    message = b'encrypting is just as useful'
    token = encrypt(key, message)
    print(token)
