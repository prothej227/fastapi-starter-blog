from models import Blog
from sqlalchemy.orm import Session
from schemas import ShowBlog, BlogSchema
from fastapi import status, HTTPException
from typing import Dict, List

def all(db: Session):
    blogs = db.query(Blog).all()
    return blogs

def create(db: Session, request: BlogSchema) -> List[ShowBlog]:
    new_blog = Blog(
        title=request.title,
        body=request.body,
        active_flag=request.active_flag,
        user_id = 1
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(db: Session, id: int) -> ShowBlog:
    blog = db.query(Blog).filter_by(id=id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} cannot be found.")
    return blog

def purge(db: Session, id: int) -> Dict:
    blog = db.query(Blog).filter_by(id=id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} cannot be found.")
    db.delete(blog)
    db.commit()
    return {
        "detail": f"Blog with id {id} has been deleted successfully."
    }

def update(db: Session, id: int, request: BlogSchema) -> Dict:
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} cannot be found."
        )
    blog.update(request.model_dump())
    db.commit()
    return  {
        "detail": f"Blog with id {id} has been updated successfully."
    }