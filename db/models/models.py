from sqlalchemy import (
    Boolean, Column, ForeignKey,
    Integer, String, DateTime,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType

from datetime import datetime

from db.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    email = Column(EmailType)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    post = relationship("Post", back_populates="owner")
    comment = relationship("Comment", back_populates="owner_comment")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="post")
    post_comment = relationship("Comment", back_populates="post_related")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    message = Column(Text)
    owner_id = Column(Integer, ForeignKey("core.users.id", ondelete="CASCADE"))
    post_id = Column(Integer, ForeignKey("core.posts.id", ondelete="CASCADE"))

    owner_comment = relationship("User", back_populates="comment")
    post_related = relationship("Post", back_populates="post_comment")
