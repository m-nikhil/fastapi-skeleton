from enum import Enum
from pydantic import EmailStr, BaseModel
from pydantic.types import constr


class RoleEnum(str, Enum):
    admin = 'admin'
    job_seeker = 'seeker'
    job_provider = 'provider'


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: str
    phone: constr(strip_whitespace=True, max_length=10)
    role: RoleEnum
    active: bool

    class Config:
        orm_mode = True


class UserRequest(User):
    password: str


class UserResponse(User):
    pass


class UserPersist(User):
    hashed_password: str
