from sqlalchemy.orm import Session, joinedload

from db import models, schemas


def create_post(db: Session, post: schemas.PostCreate, user: schemas.User):
    """
    служебная функция для создания поста
    """
    db_post = models.Post(**post.dict(), owner=user)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db: Session, id: int):
    """
    служебная функция отображение конктретного поста
    """
    return db.query(models.Post).options(joinedload(models.Post.owner).load_only(
        "username", "email")).filter(models.Post.id == id).first()


def post_list(db: Session):
    """
    служебная функция для отображения всех постов
    """
    return db.query(models.Post).options(joinedload(models.Post.owner).load_only(
        "username", "email")).all()
