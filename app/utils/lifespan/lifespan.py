from starlette.types import ASGIApp
from contextlib import asynccontextmanager
from services.broker import KafkaClient


@asynccontextmanager
async def lifespan(app: ASGIApp):
    consumer = KafkaClient.get_consumer()
    await consumer.start()
    await KafkaClient.mail_broadcast(consumer=consumer)
    yield
    await consumer.stop()