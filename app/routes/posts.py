from .. import database, models, schemas
from ..services import crud, auth

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session


router = APIRouter(
    tags=['Blogs']
)

get_db = database.get_db


@router.post("/posts/create", status_code=status.HTTP_201_CREATED)
def create_post_for_user(
        post: schemas.PostCreate, db: Session = Depends(get_db),
        current_user: models.User = Depends(auth.get_current_user)
):
    """
    Данндая функция для создании поста
    """
    user = current_user
    return crud.create_post(db=db, post=post, user=user)


@router.get("/posts/all")
def post_list(db: Session = Depends(get_db)):
    """
    Данндая функция возврашает все данные c поста
    """
    return crud.post_list(db=db)


@router.post("/posts/{post_id}/comment", response_model=schemas.CommentList)
def create_comment(comment: schemas.CommentBase,
                   post_id: int,
                   db: Session = Depends(get_db),
                   ):

    return crud.create_comment(db=db, post_id=post_id, comment=comment)


@router.get("/posts/{post_id}")
def post_detail(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_posts(db=db, id=post_id)
    comment = db.query(models.Comment).filter(models.Comment.post_id == post_id)
    active_comment = comment.filter(models.Comment.is_active == True).all()

    if post is None:
        raise HTTPException(status_code=404, detail="post does not exist")
    return {"post": post, "active_comment": active_comment}
