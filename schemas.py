from pydantic import BaseModel
from typing import Optional, List

class BlogSchema(BaseModel):
    title: str
    body: str
    active_flag : Optional[bool]
    class Config():
        from_attributes = True

class ShowUserSchema(BaseModel):
    username: str
    email: str
    blog: List[BlogSchema]
    class Config():
        from_attributes = True

class ShowBlog(BaseModel):
    title: str
    body: str
    author: ShowUserSchema
    class Config():
        from_attributes = True

class UserSchema(BaseModel):
    username: str
    email: str
    password: str