from typing import List, Union

from pydantic import BaseModel


class ItemBase(BaseModel):
    """base schema for Item model"""
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    """schema class for creating Item"""
    pass


class Item(ItemBase):
    """schema class for reading Item data"""
    id: int
    owner_id: int

    class Config:
        orm_mode = True


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
        orm_mode = True
