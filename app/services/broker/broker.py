from services.broker.base import BaseBrokerClient
from aiokafka import AIOKafkaConsumer
from core.settings import get_settings
from services.mail.MailSender import MailService
import json
from core.logger import logger

broker_settings = get_settings().broker


class KafkaClient(BaseBrokerClient):

    @classmethod
    def get_consumer(*args) -> AIOKafkaConsumer:
        return AIOKafkaConsumer(
            "mails", 
            group_id="Notification group",
            bootstrap_servers=broker_settings.url
        )

    @classmethod
    async def mail_broadcast(cls, consumer: AIOKafkaConsumer):
        async for update in consumer:
            logger.info("Consume new update")
            value = json.loads(update.value.decode())
            async with MailService() as client:
                try:
                    await client.send_plaintext(
                        subject=value.get("subject"), 
                        message_text=value.get("message"), 
                        to_email=value.get("to_mail")
                    )
                except Exception as e:
                    logger.error(f"Error: {e}")