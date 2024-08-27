from pydantic import BaseModel, EmailStr
from typing import Annotated
from annotated_types import MinLen, MaxLen

class User(BaseModel):
    username: Annotated[str, MaxLen(3), MaxLen(23)]
    email: EmailStr
    password: str
