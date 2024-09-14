from fastapi import FastAPI

from app.config import database
from app.routers import items, users

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(users.router)
app.include_router(items.router)
