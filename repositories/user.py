from fastapi import status, HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from models import User
from schemas import UserSchema

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create(db: Session, request: UserSchema):
    hashed_pwd = pwd_cxt.hash(request.password)
    new_user = User(**request.model_dump())
    new_user.password = hashed_pwd
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(db: Session, id: int):
    user = db.query(User).filter_by(id=id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with id {id} cannot be found."
        )
    return user