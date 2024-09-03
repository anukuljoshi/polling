from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    """example with error handling"""
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}


class UnicornExceptionError(Exception):
    """custom exception class"""

    def __init__(self, name: str) -> None:
        self.name = name


@app.exception_handler(UnicornExceptionError)
async def unicorn_exception_handler(
    request: Request, exc: UnicornExceptionError
):
    """handler function for exception"""
    return JSONResponse(
        status_code=418,
        content={
            "message": (
                f"Oops! {exc.name} did something. There goes a rainbow..."
            )
        },
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    """read unicorn from path param

    Args:
    ----
        name: name of the unicorn

    Raises:
    ------
        UnicornExceptionError: custom exception

    Returns:
    -------
        details of the unicorn
    """
    """example with custom exception"""
    if name == "yolo":
        raise UnicornExceptionError(name=name)
    return {"unicorn_name": name}
