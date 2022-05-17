from datetime import timedelta

from db import schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

from db.database import get_db
from db.models import models
from services import oauth2
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Users'],
    prefix='/users',
)

ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = oauth2.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = oauth2.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me")
async def read_users_me(current_user: models.User = Depends(oauth2.get_current_user)):
    return current_user


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)):
    sign_up_user = oauth2.get_user(db, username=user.username)
    if sign_up_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        create_user = oauth2.create_user(db=db, user=user)
    return f"you have successfully sign up {create_user.username}"
