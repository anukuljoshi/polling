from sqlalchemy.orm import Session

from app.models import items as item_models
from app.schemas import items as item_schemas


def get_items(db: Session, skip: int = 0, limit: int = 100):
    """get list of items"""
    return db.query(item_models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: item_schemas.ItemCreate, user_id: int):
    """create item for a user"""
    db_item = item_models.Item(**item.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
