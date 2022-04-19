from sqlalchemy.orm import Session, joinedload

from post_app import schemas, models


def create_post(db: Session, post: schemas.PostCreate, user: schemas.User):
    """
    служебная функция для создания поста
    """
    db_post = models.Post(**post.dict(), owner=user)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_posts(db: Session, id: int):
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


def create_comment(db: Session, post_id: int, comment: schemas.CommentBase, user: schemas.User):
    """
    служебная функция для комментарии конктретного поста
    """
    db_comment = models.Comment(post_id=post_id, **comment.dict(), owner_comment=user)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
