from fastapi import APIRouter

from users.schemas import User
from users.crud import create_user, get_users

router = APIRouter(
    prefix="/user",
    tags=["user"],

)


@router.post("/add_user/")
async def add_user(user: User):
    user = create_user(user)
    return user


@router.get("/get_users/")
def get_all_users():
    return get_users()
