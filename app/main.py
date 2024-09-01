"""base file for the application."""

from typing import List, Set, Union

from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.networks import HttpUrl

app = FastAPI()


class Image(BaseModel):
    """model for Image"""

    url: HttpUrl
    name: str


class Item(BaseModel):
    """model for Item"""

    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    image: Union[Image, None] = None
    images: Union[List[Image], None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """example 1 for nested models"""
    results = {"item_id": item_id, "item": item}
    return results


class Offer(BaseModel):
    """model for Offer"""

    name: str
    description: Union[str, None] = None
    price: float
    items: List[Item]


@app.post("/offers/")
async def create_offer(offer: Offer):
    """example 2 for nested models"""
    return offer
