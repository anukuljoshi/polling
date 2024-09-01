from typing import Any, List, Union

from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.networks import EmailStr

app = FastAPI()


class Item(BaseModel):
    """model class for Item"""
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    """example 1 with response return type"""
    return item


@app.get("/items/")
async def read_items() -> List[Item]:
    """example 2 with response return type"""
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]


@app.post("/items/", response_model=Item)
async def create_item2(item: Item) -> Any:
    """example 1 with response_model"""
    return item


@app.get("/items/", response_model=List[Item])
async def read_items2() -> Any:
    """example 2 with response_model"""
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]


class UserIn(BaseModel):
    """model class for UserIn"""
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    """model class for UserOut"""
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    """example 1 with hidden data in response"""
    return user


class BaseUser(BaseModel):
    """model class for base user"""
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserIn(BaseUser):
    """model class for UserIn"""
    password: str


@app.post("/user/")
async def create_user2(user: UserIn) -> BaseUser:
    """example 2 with hidden data in response"""
    return user
