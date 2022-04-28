from sqlalchemy import and_
from sqlalchemy.orm import Session, joinedload
from fastapi import APIRouter, Depends, status, HTTPException

from db import models, database, schemas
from db.models import models
from db.schemas import User
from services import crud, oauth2


router = APIRouter(
    tags=['Blogs']
)

get_db = database.get_db


@router.post("/posts/create", status_code=status.HTTP_201_CREATED)
def create_post_for_user(
        post: schemas.PostCreate, db: Session = Depends(get_db),
        current_user: models.User = Depends(oauth2.get_current_user)
):
    """
    Для создания поста
    """
    user = current_user
    return crud.create_post(db=db, post=post, user=user)


@router.get("/posts/all")
def post_list(db: Session = Depends(get_db)):
    """
    Для вывода всех постов
    """
    return crud.post_list(db=db)


@router.post("/posts/{post_id}/comment", response_model=schemas.CommentList)
def create_comment(comment: schemas.CommentBase,
                   post_id: int, db: Session = Depends(get_db),
                   current_user: models.User = Depends(oauth2.get_current_user)
                   ):
    """
    Для создании комментариев
    """
    user = current_user
    return crud.create_comment(db=db, post_id=post_id, comment=comment, user=user)


@router.get("/posts/{post_id}")
def post_detail(post_id: int, db: Session = Depends(get_db)):
    """
    Для получение инфо одного поста
    """
    post = crud.get_posts(db=db, id=post_id)
    comments = db.query(models.Comment).options(
        joinedload(models.Comment.owner_comment).load_only("username", "email")
    ).filter(
        and_(
            models.Comment.post_id == post_id,
            models.Comment.is_active == True
        )
    ).all()

    if post is None:
        raise HTTPException(status_code=404, detail="post_app does not exist")
    return {"post_app": post, "comments": comments}
