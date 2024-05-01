from pydantic import BaseModel
from src.routes.users.models import User

class SaveUserRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

    def to_model(self):
        user = User()
        user.first_name = self.first_name
        user.last_name = self.last_name
        user.email = self.email
        user.password = self.password
        return user
