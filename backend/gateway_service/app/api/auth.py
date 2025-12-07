from fastapi import APIRouter
from app.core.config import settings


router = APIRouter(prefix="/auth")


@router.post("/login")
async def login():
    pass
