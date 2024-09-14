from sqlalchemy.orm import Session

from app.models import users as user_models
from app.schemas import users as user_schemas


def get_user(db: Session, user_id: int):
    """get user data with user_id"""
    return (
        db.query(user_models.User)
        .filter(user_models.User.id == user_id)
        .first()
    )


def get_user_by_email(db: Session, email: str):
    """get user data with email"""
    return (
        db.query(user_models.User)
        .filter(user_models.User.email == email)
        .first()
    )


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """get user list"""
    return db.query(user_models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schemas.UserCreate):
    """create user"""
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = user_models.User(
        email=user.email, hashed_password=fake_hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
