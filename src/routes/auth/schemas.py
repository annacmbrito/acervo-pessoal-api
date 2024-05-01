from pydantic import BaseModel, EmailStr, Field

class LoginRequest(BaseModel):
    email: EmailStr = Field(..., max_length=64)
    password: str = Field(..., min_length=8, max_length=128, pattern="^[a-zA-Z0-9]*[a-zA-Z]+[0-9]+[a-zA-Z0-9]*$")

class LoginResponse(BaseModel):
    token: str