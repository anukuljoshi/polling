from typing import List

from fastapi import HTTPException
from fastapi.routing import APIRouter

from app.dependencies import DataBaseDependency
from app.schemas import users as user_schemas
from app.services import users as user_services

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/users/", response_model=user_schemas.User)
def create_user(db: DataBaseDependency, user: user_schemas.UserCreate):
    """handler for creating user"""
    db_user = user_services.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_services.create_user(db=db, user=user)


@router.get("/users/", response_model=List[user_schemas.User])
def read_users(db: DataBaseDependency, skip: int = 0, limit: int = 100):
    """handler for getting user list"""
    users = user_services.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=user_schemas.User)
def read_user(db: DataBaseDependency, user_id: int):
    """handler for getting user by user_id"""
    db_user = user_services.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
