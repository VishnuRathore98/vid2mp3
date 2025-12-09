from fastapi import APIRouter
from app.core.auth_core import user_login


router = APIRouter(prefix="/auth")


@router.post("/login")
async def login(request):
    """
    Login the user using valid credentials.
    """
    response = user_login(request)
    return response
