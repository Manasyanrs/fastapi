import uvicorn
from fastapi import FastAPI

from users.views import router as user_router
from items.views import router as item_router

app = FastAPI(
    title="fastapi testing",
    description="Description of the FastAPI testing",
    version="0.1.0",
)

app.include_router(user_router)
app.include_router(item_router)


@app.get("/")
async def home_page():
    """
    home page info
    :return: str
    """
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
