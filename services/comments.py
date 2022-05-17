from sqlalchemy.orm import Session

from db import schemas
from db.models import models


def create_comment(db: Session, post_id: int, comment: schemas.CommentBase, user: schemas.User):
    """
    служебная функция для комментарии конктретного поста
    """
    db_comment = models.Comment(post_id=post_id, **comment.dict(), owner_comment=user)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
