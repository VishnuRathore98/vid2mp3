from fastapi import APIRouter
from app.utils.email_util import send_mail

router = APIRouter(prefix="/api/v1/notification")


@router.post("/send_mail")
async def email(sender:str, receipient: str, data: str):
    # send mail to sender from receipient with data
    pass
    
