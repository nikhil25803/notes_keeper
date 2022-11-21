from pydantic import BaseModel
from datetime import datetime
from typing import List


class UserBase(BaseModel):
    name: str
    email: str
    password: str

class Notes(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True

class UserDisplay(BaseModel):
    name: str
    email: str
    posts:List[Notes]

    class Config:
        orm_mode = True


class NotesBase(BaseModel):
    title: str
    description: str
    user_id: int


class NotesDisplay(BaseModel):
    id: int
    title: str
    description: str
    user = UserDisplay

    class Config:
        orm_mode = True
