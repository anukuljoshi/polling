"""base file for the application."""

from typing import Union

from fastapi import FastAPI

app = FastAPI()


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

    Returns: data with item_id

    """
    return {"item_id": item_id, "q": q}
