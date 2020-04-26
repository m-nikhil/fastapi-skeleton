from pydantic import BaseModel
from pydantic import EmailStr


class CreateUser(BaseModel):
    email: EmailStr
    full_name: str
    password: str
