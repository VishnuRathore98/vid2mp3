from fastapi import APIRouter
from app.utils.messaging import channel
from app.services.file_service import file_upload


router = APIRouter(prefix="/file")


@router.post("/upload")
async def upload():
    """
    This end point will be responsible for file upload.
    """
    fd = "file descriptor"
    gfs = "gridfs instance"
    uid = "user id from access token"
    response = file_upload(
        file_descriptor=fd,
        gridfs=gfs,
        channel=channel,
        user_id=uid,
    )
    return response
