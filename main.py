import uvicorn
from fastapi import FastAPI

from models.user_model import User

app = FastAPI(
    title="fastapi testing",
    description="Description of the FastAPI testing",
    version="0.1.0",
)


@app.post("/add_user/")
async def add_user(user: User):
    return {
        "message": "User added successfully!",
        "user": user.email
    }


@app.get("/")
async def home_page():
    """
    home page info
    :return:
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def get_item_by_id(item_id: int):
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
