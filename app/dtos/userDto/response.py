from pydantic import BaseModel
from pydantic import EmailStr


class ResponseUser(BaseModel):
    email: EmailStr
    full_name: str
