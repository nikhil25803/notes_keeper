from fastapi import APIRouter, Depends, HTTPException, status
from .schema import NotesBase, NotesDisplay, NotesUpdate
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import models
from controllers import post_controllers
from auth.oauth2 import get_current_user
from routes.schema import UserAuth


router = APIRouter(prefix="/post", tags=["posts"])


@router.post("", response_model=NotesDisplay)
def create_notes(
    request: NotesBase,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):
    return post_controllers.create_post(db, request)


@router.delete("/delete/{user_id}/{post_id}")
def delete_node(
    user_id: int,
    id: int,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):
    return post_controllers.delete_post(db=db, id=id, user_id=current_user.id)


@router.patch("/update/{user_id}/{post_id}")
def update_note(
    post_id: int,
    user_id: int,
    request:NotesUpdate,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):
    post = db.query(models.NotesDB).get(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if int(current_user.id) != user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    post.title = request.title
    post.description = request.description
    db.commit()
    return post

