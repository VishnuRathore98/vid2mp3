import smtplib
import smtplib
import json
from app.core.config import settings
from email.message import EmailMessage


def send_mail(message: dict):
    try:
        message = json.loads(message)
        mp3_fid = message["mp3_fid"]
        sender_address = settings.SENDER_ADDRESS
        sender_password = settings.SENDER_PASSWORD
        receiver_addess = message["user_email"]

        emsg = EmailMessage()
        emsg.set_content(f"mp3 file: {mp3_fid} now available to download!")
        emsg["Subject"] = "MP3 download"
        emsg["From"] = sender_address
        emsg["To"] = receiver_addess

        session = smtplib.SMTP("smtp.gmail.com")
        session.starttls()
        session.login(user=sender_address, password=sender_password)
        session.send_message(
            msg=emsg, from_addr=sender_address, to_addrs=receiver_addess
        )
        session.quit()
        print("Mail sent!")

    except Exception as e:
        print("Exception: ", e)
        return e
