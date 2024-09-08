from typing import Union

from fastapi import Depends, FastAPI
from typing_extensions import Annotated

app = FastAPI()


async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
) -> "dict[str, Union[str, int, None]]":
    """example of a dependency function"""
    return {"q": q, "skip": skip, "limit": limit}


CommonDeps = Annotated[
    "dict[str, Union[str, int, None]]", Depends(common_parameters)
]


@app.get("/items/")
async def read_items(commons: CommonDeps):
    """example 1 with dependency"""
    return commons


@app.get("/users/")
async def read_users(commons: CommonDeps):
    """example 2 with dependency"""
    return commons
