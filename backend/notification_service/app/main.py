from fastapi import FastAPI
from app.api.v1 import notification

app = FastAPI()


@app.get("/")
def notification_root():
    return {"message": "welcome to notification service!"}


app.include_router(notification.router)
