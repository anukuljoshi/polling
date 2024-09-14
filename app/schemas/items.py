from typing import Union

from pydantic.main import BaseModel


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
        from_attributes = True
