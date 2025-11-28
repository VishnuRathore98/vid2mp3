from fastapi import APIRouter, Depends, HTTPException, status
from jose import jwt
from sqlalchemy.orm import Session
from app.auth.jwt import create_access_token
from app.auth.password import verify_password
from app.database import get_db
from app.repositories.user_repository import get_user_by_email
from app.schemas import user_schemas


router = APIRouter(prefix="/auth/v1", tags=["Auth"])

@router.post("/login", status_code=status.HTTP_200_OK)
async def login(user_data: user_schemas.UserLogin, db: Session = Depends(get_db)):
    user = get_user_by_email(user_data.email, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid user credentials!",)

    if not verify_password(user_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "Invalid user credentials",)

    data = {"user_id": str(user.user_id)}
    access_token = create_access_token(data)

    return {"token":access_token, "token_type":"Bearer"}
