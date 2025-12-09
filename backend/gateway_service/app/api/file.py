from fastapi import APIRouter

from app.core.file_core import file_upload


router = APIRouter(prefix="/file")


@router.post("/upload")
async def upload():
    """
    This end point will be responsible for file upload.
    """
    response = file_upload()
    return response
