from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from models.models import User
from models.schemas import UserModel, Token
from utils import bcrypt_context, get_db, authenticate_user, create_token
from typing import Annotated
from database.db import Session
from starlette import status


auth_router = APIRouter(
    prefix = "/auth",
    tags = ["Authentication"],
)


db_dependency = Annotated[Session, Depends(get_db)]


@auth_router.get("/")
def index():
    return {
        "data": "This is the index route of auth router"
    }

@auth_router.post("/create-user", response_model=UserModel, status_code=status.HTTP_201_CREATED)
def create_user(db: db_dependency, user: UserModel):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User with {user.username} already exists"
        )
    db_email = db.query(User).filter(User.email == user.email).first()
    if db_email is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User with {user.email} already exists"
        )

    new_user = User(
        username = user.username,
        email = user.email,
        password = bcrypt_context.hash(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return user

@auth_router.post("/login")
def login(db: db_dependency, form: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form.username, form.password, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User doesn't exist"
        )
    
    token = create_token(user.id, user.username, timedelta(minutes=30))
    return Token(
        token=token,
        token_type="bearer"
    )

