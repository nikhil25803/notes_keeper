from routes.schema import NotesBase
from sqlalchemy.orm.session import Session
from db.models import NotesDB
from datetime import datetime
from auth.oauth2 import get_current_user
from routes.schema import UserAuth
from fastapi import Depends


def create_post(db: Session, request: NotesBase, current_user:UserAuth=Depends(get_current_user)):
    new_post = NotesDB(
        title=request.title,
        description=request.description,
        user_id = request.user_id,
        created_at=datetime.now(),
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
