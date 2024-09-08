from typing import Union

from fastapi import Depends, FastAPI
from typing_extensions import Annotated

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]


class CommonQueryParams:
    """class for defining common query params"""

    def __init__(
        self, q: Union[str, None] = None, skip: int = 0, limit: int = 100
    ) -> None:
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(
    commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)],
):
    """example 1 with class as dependency"""
    response = {}
    if commons.q:
        response["q"] = commons.q

    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response["items"] = items
    return items
