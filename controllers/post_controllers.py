from routes.schema import NotesBase, NotesUpdate
from sqlalchemy.orm.session import Session
from db.models import NotesDB
from db.database import get_db
from datetime import datetime
from auth.oauth2 import get_current_user
from routes.schema import UserAuth
from fastapi import Depends, HTTPException, status


def create_post(db: Session, request: NotesBase):
    new_post = NotesDB(
        title=request.title,
        description=request.description,
        user_id=request.user_id,
        created_at=datetime.now(),
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def delete_post(db: Session, id: int, user_id:int):
    post = db.query(NotesDB).filter(NotesDB.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post of id:{id} doesn't exist",
        )
    if int(post.user_id) != user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Only the user created this post can delete."
        )
    db.delete(post)
    db.commit()
    return 'Post Deleted'

# def update_notes(db:Session, id:int,user_id:int, request:NotesUpdate):
#     post = db.query(NotesDB).filter(NotesDB.id==id).first()
#     if not post:
#         return HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Post with id:{id} not found"
#         )
#     if int(post.user_id)!=user_id:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="You are not authorize this resource"
#         )
#     post_data = request.dict(exclude_unset=True)
#     print("Done 1")
#     for key, value in post_data.items():
#             setattr(post, key, value)

#     db.add(post)
#     db.commit()
#     db.refresh(post)
#     return post
