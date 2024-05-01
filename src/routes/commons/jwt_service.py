from jose import jwt as jwt_jose, JWTError

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
        
    def get_user_email(self, token: str):
        return self.get_claim(token, self.USER_EMAIL_KEY)
    
    def get_claim(self, token: str, claim: str):
            claims = self.get_claims(token)

            expiration_time = claims.get(self.EXPIRATION_KEY, 0)
            current_time = round(time.time() * 1000)

            if expiration_time < current_time:
                raise ValueError("Token expired")
            
            result = claims.get(claim)
            
            if result is None:
                raise ValueError("Invalid token")
            return result
    
    def get_claims(self, token: str):
        try:
            return jwt_jose.decode(
                token, 
                key=self.JWT_SECRET, 
                algorithms=["HS256"]
            )
        except JWTError:
            raise ValueError("Invalid token")

jwt = JwtService()