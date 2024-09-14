from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing_extensions import Annotated

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    """middleware to get db instance in handlers"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DataBaseDependency = Annotated[Session, Depends(get_db)]


@app.post("/users/", response_model=schemas.User)
def create_user(db: DataBaseDependency, user: schemas.UserCreate):
    """handler for creating user"""
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(db: DataBaseDependency, skip: int = 0, limit: int = 100):
    """handler for getting user list"""
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(db: DataBaseDependency, user_id: int):
    """handler for getting user by user_id"""
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    db: DataBaseDependency, user_id: int, item: schemas.ItemCreate
):
    """handler for creating items for a user"""
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(db: DataBaseDependency, skip: int = 0, limit: int = 100):
    """handler for getting list of items"""
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
