from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    full_name: str
    password: str

class UserRequest(UserBase):
    password: str

class UserResponse(UserBase):
    pass

class UserPersist(UserBase):
    hashed_password: str


