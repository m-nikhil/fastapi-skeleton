from pydantic import BaseModel
from pydantic import EmailStr


class User(BaseModel):
    id: int = None
    email: EmailStr
    full_name: str
    hashed_password: str

    class Config:
        orm_mode = True
