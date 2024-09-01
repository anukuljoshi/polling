"""base file for the application."""

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    """model class for request body"""

    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.post("/items")
def create_item(item: Item):
    """create a new item

    Args:
    ----
        item (Item): data for item

    Returns:
    -------
        created item
    """
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({
            "price_with_tax": price_with_tax
        })
    return item_dict
