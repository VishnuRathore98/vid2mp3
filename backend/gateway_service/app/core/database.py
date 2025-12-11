from pymongo import MongoClient
from gridfs import GridFSBucket
from app.core.config import settings


CONNECTION_STRING = settings.MONGODB_URL


async def get_db():
    client = MongoClient(CONNECTION_STRING)
    videos_db = client["videos_db"]
    bucket = GridFSBucket(videos_db)

    return bucket
