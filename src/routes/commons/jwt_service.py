import os

class JwtService:
    JWT_SECRET = os.getenv('JWT_SECRET')
    JWT_EXPIRATION_IN_MILLISECONDS = int(os.getenv('JWT_EXPIRATION_IN_MILLISECONDS'))
    USER_EMAIL_KEY: str = "email"
    EXPIRATION_KEY: str = "expiration"

jwt = JwtService()