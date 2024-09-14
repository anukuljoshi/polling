from typing import List

from fastapi.routing import APIRouter

from app.dependencies import DataBaseDependency
from app.schemas import items as item_schemas
from app.services import items as item_services

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.get("/items/", response_model=List[item_schemas.Item])
def read_items(db: DataBaseDependency, skip: int = 0, limit: int = 100):
    """handler for getting list of items"""
    items = item_services.get_items(db, skip=skip, limit=limit)
    return items


@router.post("/users/{user_id}/items/", response_model=item_schemas.Item)
def create_item_for_user(
    db: DataBaseDependency, user_id: int, item: item_schemas.ItemCreate
):
    """handler for creating items for a user"""
    return item_services.create_user_item(db=db, item=item, user_id=user_id)
