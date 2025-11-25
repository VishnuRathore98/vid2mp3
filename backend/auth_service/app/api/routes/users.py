from fastapi import APIRouter, status, Depends
from app.database import get_db, engine
from app.schemas import user_schemas
from app.models import user_models


router = APIRouter(
    prefix="/auth/v1",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserOut,
)


@router.post("/register")
async def register_user(data: UserIn, db: Session = Depends(get_db)): ...
