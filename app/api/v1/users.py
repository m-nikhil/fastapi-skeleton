from fastapi import APIRouter

router = APIRouter()


@router.get("/users/")
async def read():
    return [{"username": "Foo"}, {"username": "Bar"}]


@router.get("/users/me")
async def read_me():
    return {"username": "fakecurrentuser"}



