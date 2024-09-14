from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from typing_extensions import Annotated

from app.config.database import SessionLocal


def get_db():
    """middleware to get db instance in handlers"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DataBaseDependency = Annotated[Session, Depends(get_db)]
