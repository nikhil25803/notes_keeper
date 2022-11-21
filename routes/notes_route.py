from fastapi import APIRouter, Depends
from .schema import NotesBase, NotesDisplay
from sqlalchemy.orm.session import Session
from db.database import get_db
from controllers import post_controllers


router = APIRouter(
    prefix='/post',
    tags=['posts']
)


@router.post('',response_model=NotesDisplay)
def create_notes(request:NotesBase, db:Session = Depends(get_db)):
    return post_controllers.create_post(db, request)