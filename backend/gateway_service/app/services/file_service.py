import json
import pika


async def file_upload(file_descriptor, gridfs, channel, user_id):
    """
    This method will be responsible for the file upload functionality.
    """
    try:
        fid = gridfs.put(file_descriptor)
    except Exception as err:
        return err

    message = {
        "video_fid": str(file_descriptor),
        "mp3_fid": None,
        "user_id": user_id,
    }

    try:
        channel.basic_publish(
            exhange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent,
            ),
        )
    except:
        gridfs.delete(fid)
        return "error"


async def file_download():
    """
    This method will be responsible for the file download functionality.
    """
