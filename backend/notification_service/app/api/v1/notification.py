from fastapi import APIRouter
from app.utils.email_util import send_mail

router = APIRouter(prefix="/api/v1/notification")


@router.post("/send_mail")
async def email():
    # send mail to sender from receipient with data

    send_mail()
