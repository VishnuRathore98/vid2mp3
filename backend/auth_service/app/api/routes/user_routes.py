from fastapi import APIRouter, status, Depends
from app.database import get_db
from app.schemas import user_schemas
from sqlalchemy.orm import Session
from app.utils.security import get_current_user


router = APIRouter(prefix="/auth/v1", tags=["Users"])


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=user_schemas.UserOut,
)
async def register_user(
    data: user_schemas.UserRegister,
    db: Session = Depends(get_db),
): ...


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
