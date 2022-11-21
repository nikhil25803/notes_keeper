from .database import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey



class UserDb(Base):
    __tablename__="user"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    email = Column(String)
    password=Column(String)
    posts = relationship("NotesDB", back_populates="user")



class NotesDB(Base):
    __tablename__="notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("UserDb", back_populates="posts")
