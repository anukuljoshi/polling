"""base file for the application."""

from typing import Any, Union

from fastapi import FastAPI, Path
from pydantic import BaseModel
from pydantic.fields import Field
from typing_extensions import Annotated

app = FastAPI()


class Item(BaseModel):
    """model for Item"""

    name: str
    description: Union[str, None] = Field(
        default=None, description="description for the item", max_length=300
    )
    price: float = Field(gt=0, description="price of the item")
    tax: Union[float, None] = None


@app.get("/items/{item_id}")
def update_item(
    item_id: Annotated[
        int, Path(description="The ID of the item to get", gt=0, le=1000)
    ],
    q: Union[str, None] = None,
    item: Union[Item, None] = None,
):
    """example with Path, Query and Body"""
    results: Any = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results
