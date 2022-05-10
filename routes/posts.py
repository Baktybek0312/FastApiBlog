from sqlalchemy import and_
from sqlalchemy.orm import Session, joinedload
from fastapi import APIRouter, Depends, status, HTTPException

from db import models, database, schemas
from db.models import models
from services import posts, oauth2, comments


router = APIRouter(
    tags=['Blogs'],
    prefix='/posts'
)

get_db = database.get_db


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_post_for_user(
        post: schemas.PostCreate, db: Session = Depends(get_db),
        current_user: models.User = Depends(oauth2.get_current_user)
):
    """
    Для создания поста
    """
    user = current_user
    return posts.create_post(db=db, post=post, user=user)


@router.get("/list")
def post_list(db: Session = Depends(get_db)):
    """
    Для вывода всех постов
    """
    return posts.post_list(db=db)


@router.post("/{post_id}/comments", response_model=schemas.CommentList)
def create_comment(comment: schemas.CommentBase,
                   post_id: int, db: Session = Depends(get_db),
                   current_user: models.User = Depends(oauth2.get_current_user)
                   ):
    """
    Для создании комментариев
    """
    user = current_user
    return comments.create_comment(db=db, post_id=post_id, comment=comment, user=user)


@router.get("/{post_id}")
def post_detail(post_id: int, db: Session = Depends(get_db)):
    """
    Для получение инфо одного поста
    """
    post = posts.get_post(db=db, id=post_id)
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
