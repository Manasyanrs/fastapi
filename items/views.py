from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["items"],
)

@router.get("/{item_id}")
async def get_item_by_id(item_id: int):
    return {"item_id": item_id}