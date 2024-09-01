"""base file for the application."""

from typing import Any, Union

from fastapi import Body, FastAPI, Path
from pydantic import BaseModel
from typing_extensions import Annotated

app = FastAPI()


class Item(BaseModel):
    """model for Item
    """
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.get("/items/{item_id}")
def update_item(
    item_id: Annotated[
        int, Path(description="The ID of the item to get", gt=0, le=1000)
    ],
    q: Union[str, None] = None,
    item: Union[Item, None] = None,
):
    """example with Path, Query and Body
    """
    results: Any = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


class User(BaseModel):
    """model for Item
    """
    username: str
    fullname: Union[str, None] = None


@app.get("/items/user/{item_id}")
def update_item_user(
    item_id: Annotated[
        int, Path(description="The ID of the item to get", gt=0, le=1000)
    ],
    item: Item,
    user: User,
    importance: Annotated[int, Body()]
):
    """example with multiple body params
    """
    results: Any = {
        "item_id": item_id,
        "item": item,
        "user": user,
        "importance": importance,
    }
    return results


@app.get("/items/embed/{item_id}")
def update_item_embed(
    item_id: Annotated[
        int, Path(description="The ID of the item to get", gt=0, le=1000)
    ],
    item: Annotated[Item, Body(embed=True)],
):
    """example with multiple body params
    """
    results: Any = {
        "item_id": item_id,
        "item": item,
    }
    return results
