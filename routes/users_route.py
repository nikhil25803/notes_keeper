from fastapi import APIRouter, Depends
from .schema import UserDisplay, UserBase
from sqlalchemy.orm.session import Session
from db.database import get_db
from controllers import user_controller
from auth.oauth2 import get_current_user
from routes.schema import UserAuth




router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('', response_model=UserDisplay)
def create_user(request:UserBase, db:Session = Depends(get_db)):
    return user_controller.create_user(db, request)


@router.get('/{username}', response_model=UserDisplay)
def get_user(username:str, db:Session=Depends(get_db), current_user:UserAuth =Depends(get_current_user)):
    return user_controller.get_user(db,username)