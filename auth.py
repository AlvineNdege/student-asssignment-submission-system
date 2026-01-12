from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import RegisterSchema, LoginSchema
from app.core.security import (
    hash_password, verify_password,
    create_access_token, create_refresh_token
)
from app.core.config import settings
from app.core.dependencies import get_db
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(data: RegisterSchema, db: Session = Depends(get_db)):
    if data.role == "teacher" and data.admin_code != settings.ADMIN_CODE:
        raise HTTPException(403, "Invalid admin code")

    user = User(
        name=data.name,
        email=data.email,
        password_hash=hash_password(data.password),
        role=data.role
    )
    db.add(user)
    db.commit()
    return {"message": "Registration successful"}

@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(401, "Invalid credentials")

    return {
        "access_token": create_access_token({"sub": user.id, "role": user.role}),
        "refresh_token": create_refresh_token({"sub": user.id})
    }
