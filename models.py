from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    active_flag = Column(Boolean)
    user_id = Column(Integer, ForeignKey('user.id'))
    author = relationship("User", back_populates="blog")

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    active_flag = Column(Boolean, default=True)
    blog = relationship('Blog', back_populates="author")