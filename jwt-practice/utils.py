from fastapi import HTTPException, Depends
from typing import Annotated
from starlette import status
from jose import jwt, JWTError 
from datetime import datetime, timedelta
from models.models import User
from models.schemas import Token
from database.db import Base, engine, Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = 'dd7381b6385a4308695f416342732bf8aee495e8c96f5294b3b38454132094aa'
ALGORITHM = 'HS256'
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

def authenticate_user(username: str, password: str, db: db_dependency):
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user or not bcrypt_context.verify(password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid User Credentials"
        )
    return db_user

def create_token(user_id: int, username: str, expiry_time: timedelta = timedelta(minutes=30)):
    to_encode = {
        'id': user_id,
        'user': username,
        'exp': datetime.utcnow() + expiry_time
    }
    token =  jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token


def get_current_user(token: Annotated[str, Depends(oauth2_bearer)], db: db_dependency):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("id")
        username = payload.get("user")

        if user_id is None or username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User is not authenticated"
            )
        
        db_user = db.query(User).filter(User.username == username).first()
        if db_user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User is not authenticated"
            )

        return {
            "id": db_user.id,
            "username": db_user.username,
        }
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate token"
        )
