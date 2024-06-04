from fastapi import APIRouter, Depends
from typing import Annotated
from utils import get_current_user, get_db
from database.db import Session

store_router = APIRouter(
    prefix="/store",
    tags=["Store Routes"]
)


user_dependency = Annotated[dict, Depends(get_current_user)]
db_dependency = Annotated[Session, Depends(get_db)]

@store_router.get("/")
def index():
    return {
        "data": "Store index route"
    }

@store_router.get("/test")
def test(user: user_dependency, db: db_dependency):
    return {
        "user": user,
        "database": "Database session is working"
    }