from users.schemas import User

users = []


def create_user(user: User) -> dict:
    user = user.model_dump()
    users.append(user)

    return {
        "success": True,
        "data": user,
    }


def get_users() -> list[User]:
    return users
