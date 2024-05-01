from jose import jwt as jwt_jose

import os
import time

class JwtService:
    JWT_SECRET = os.getenv('JWT_SECRET')
    JWT_EXPIRATION_IN_MILLISECONDS = int(os.getenv('JWT_EXPIRATION_IN_MILLISECONDS'))
    USER_EMAIL_KEY: str = "email"
    EXPIRATION_KEY: str = "expiration"
    
    def generate_token(self, email: str):
        return jwt_jose.encode(
            key=self.JWT_SECRET, 
            algorithm="HS256",
            claims={
                self.USER_EMAIL_KEY: email,
                self.EXPIRATION_KEY: round(time.time() * 1000) + self.JWT_EXPIRATION_IN_MILLISECONDS,
            }
        )

jwt = JwtService()