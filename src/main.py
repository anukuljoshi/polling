"""base file for the application."""

from enum import Enum
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    """model class for Item"""

    name: str
    price: float
    is_offer: Union[bool, None]


@app.get("/")
def read_root():
    """Handle home route."""
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None]):
    """Read Item with a given id.

    Args:
    ----
        item_id: id of the item
        q: query param key

    Returns:
    -------
        data with item_id

    """
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """update Item with item_id

    Args:
    ----
        item_id: id of the Item to update
        item: updated data for the Item

    Returns:
    -------
        details of the updated Item
    """
    return {
        "item_id": item_id,
        "item_name": item.name,
    }


class ModelName(str, Enum):
    """enum class for model_name"""
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/model/{model_name}")
def get_model(model_name: ModelName):
    """get model by model_name

    Args:
    ----
        model_name: name of the model

    Returns:
    -------
        detail of the model with model_name
    """
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
