from routes.schema import UserBase
from sqlalchemy.orm.session import Session
from db.models import UserDb
from db.hashing import Hash
from fastapi import HTTPException, status





def create_user(db:Session, request:UserBase):
    new_user = UserDb(
        name = request.name,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



def get_user(db:Session, id:int):
    user = db.query(UserDb).filter(UserDb.id==id).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not Found")
    else:
        return user