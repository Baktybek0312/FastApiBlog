import datetime
from typing import Optional

from pydantic import BaseModel
from fastapi import Body


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    email: str
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    description: Optional[str] = None


class PostCreate(PostBase):
    pass


class PostList(PostBase):
    created_date: Optional[datetime.datetime]
    owner: User

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    message: str


class CommentList(CommentBase):
    id: int
    post_id: int
    owner_comment: User
    created_date: Optional[datetime.datetime] = Body(None)

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
