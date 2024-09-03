from fastapi import FastAPI, Form
from typing_extensions import Annotated

app = FastAPI()


@app.post("/login/")
async def login(
    username: Annotated[str, Form()], password: Annotated[str, Form()]
):
    """example with form data"""
    return {"username": username}
