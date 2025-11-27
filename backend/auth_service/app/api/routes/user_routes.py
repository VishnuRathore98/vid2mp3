from fastapi import APIRouter, status, Depends, HTTPException
from app.database import get_db
from app.schemas import user_schemas
from app.models.user_models import User
from sqlalchemy.orm import Session
from app.auth.dependencies import get_current_user
from app.repositories.user_repository import (
    create_user,
    get_user_by_email,
    get_user_by_id,
)


router = APIRouter(prefix="/auth/v1", tags=["Users"])


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=user_schemas.UserOut,
)
async def register_user(
    user_data: user_schemas.UserRegister,
    db: Session = Depends(get_db),
):
    if await get_user_by_email(user_data.email, db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists with this email",
        )
    created_user = await create_user(user_data, db)
    return created_user


@router.get("/me", status_code=status.HTTP_200_OK, response_model=user_schemas.UserOut)
async def get_user(
    current_user: user_schemas.User = Depends(get_current_user),
): ...


@router.patch(
    "/update", status_code=status.HTTP_200_OK, response_model=user_schemas.UserOut
)
async def update_user(
    data: user_schemas.UserUpdate,
    current_user: user_schemas.User = Depends(get_current_user),
    db: Session = Depends(get_db),
): ...


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    current_user: user_schemas.User = Depends(get_current_user),
    db: Session = Depends(get_db),
): ...
