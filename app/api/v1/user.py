from fastapi import APIRouter

from app.dtos.userDto import UserRequest, UserResponse, UserPersist
from app.crud import user

router = APIRouter()


def mock_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def mock_save_user(user_request: UserRequest):
    hashed_password = mock_password_hasher(user_request.password)
    user_persist = UserPersist(**user_request.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_persist


@router.get("/user/{id}")
async def read_by_id(id: int):
    return user.get_user_by_id(id)


@router.get("/user/me", response_model=UserResponse)
async def read_me():
    return user.get_user()


@router.post("/user/", response_model=UserResponse)
async def create(user_request: UserRequest):
    user_saved = mock_save_user(user_request)
    return user_saved
