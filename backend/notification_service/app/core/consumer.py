import os
import pika
import sys
from app.core.config import settings
from app.utils.email_utils import send_mail


async def consumer():
    connection = pika.BlockingConnection(
        parameters=pika.ConnectionParameters(host="rabbitmq"),
    )
    channel = connection.channel()

    def callback(ch, method, properties, body):
        err = send_mail(body)
        if err:
            ch.basic_nack(delivey_tag=method.delivey_tag)
        else:
            ch.basic_ack(delivery_tag=method.delivey_tag)

    channel.basic_consume(
        queue=settings.MP3_QUEUE,
        on_message_callback=callback,
    )

    print("Waiting for messages, ctrl+c to exit")

    channel.start_consuming()


if __name__ == "__main__":
    try:
        result = consumer()
    except KeyboardInterrupt:
        print("Keyboard Interrupted")
        try:
            sys.exit(0)
        except:
            os._exit(0)
