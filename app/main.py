"""base file for the application."""

from typing import List, Union

from fastapi import FastAPI, Header
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[Union[str, None], Header()] = None):
    """example with Header"""
    return user_agent


@app.get("/items/x_tokens/")
async def read_items2(
    x_token: Annotated[Union[List[str], None], Header()] = None,
):
    """example with multiple Headers"""
    return {
        "X-Token Values": x_token
    }
