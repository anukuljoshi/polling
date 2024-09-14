from typing import List

from pydantic.main import BaseModel

from app.schemas.items import Item


class UserBase(BaseModel):
    """base schema class for User"""
    email: str


class UserCreate(UserBase):
    """schema class for creating User"""
    password: str


class User(UserBase):
    """schema class for reading User data"""
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        from_attributes = True
