from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password)

def are_equals_passwords(plaintext: str, hashed: str):
    return pwd_context.verify(plaintext, hashed)