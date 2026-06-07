import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_password, entered_password):
    return stored_password == hash_password(entered_password)