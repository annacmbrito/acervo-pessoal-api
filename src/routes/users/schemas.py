from pydantic import BaseModel, EmailStr, Field
from src.routes.users.models import User
from src.util.hash_password import hash_password

class SaveUserRequest(BaseModel):
    first_name: str = Field(..., min_length=3, max_length=16, pattern="^[a-zA-Z]+$")
    last_name: str = Field(..., min_length=3, max_length=16, pattern="^[a-zA-Z]+$")
    email: EmailStr = Field(..., max_length=64)
    password: str = Field(..., min_length=8, max_length=128, pattern="^[a-zA-Z0-9]*[a-zA-Z]+[0-9]+[a-zA-Z0-9]*$")

    def to_model(self):
        user = User()
        user.first_name = self.first_name
        user.last_name = self.last_name
        user.email = self.email
        user.password = hash_password(self.password)
        return user

class CurrentUserResponse(BaseModel):
    first_name: str
    last_name: str
    email: str
