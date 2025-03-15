from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from repositories import user
from schemas import ShowUserSchema, UserSchema
from database import get_db

router = APIRouter(
    prefix = "/user",
    tags = ['Users']
)

# Create User
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(request: UserSchema, db: Session = Depends(get_db)):
    return user.create(db, request)

# Show User
@router.get('/{id}', response_model=ShowUserSchema)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(db, id)