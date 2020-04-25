from typing import List

from fastapi import APIRouter

from app.dtos.userDto import UserPersist
from app.dtos.userDto import UserRequest
from app.dtos.userDto import UserResponse

router = APIRouter()

mock_data = [
    {"email": "user1@example.com", "full_name": "user one", "password": "user1 pass"},
    {"email": "user2@example.com", "full_name": "user two", "password": "user2 pass"},
]


def mock_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def mock_save_user(user_request: UserRequest):
    hashed_password = mock_password_hasher(user_request.password)
    user_persist = UserPersist(**user_request.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_persist


@router.get("/user/", response_model=List[UserResponse])
async def read():
    return mock_data


@router.get("/user/me", response_model=UserResponse)
async def read_me():
    return mock_data[0]


@router.post("/user/", response_model=UserResponse)
async def create(user_request: UserRequest):
    user_saved = mock_save_user(user_request)
    return user_saved
