from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from schemas import ShowBlog, BlogSchema
from database import get_db
from repositories import blog

router = APIRouter(
    prefix = "/blog",
    tags = ['Blogs']
)

# Get all blogs
@router.get('/', response_model=List[ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.all(db)

# Add new blog
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: BlogSchema, db: Session = Depends(get_db)):
    return blog.create(db, request)

# Get a specific blog
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    return blog.show(db, id)

# Delete a specific blog
@router.delete('/{id}', status_code=status.HTTP_200_OK)
def purge(id: int, db: Session = Depends(get_db)):
    return blog.purge(db, id)

# Update a specific blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: BlogSchema, db: Session = Depends(get_db)):
    return blog.update(db, id, request)