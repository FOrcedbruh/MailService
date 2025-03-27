from aiosmtplib import SMTP
from core.logger import logger
from core.settings import get_settings
from email.message import EmailMessage

smtp_settings = get_settings().smtp

class MailService:
    
    def __init__(self):
        self.from_email = smtp_settings.from_email
        self.smtp = SMTP(
            hostname=smtp_settings.host,
            port=smtp_settings.port, 
            password=smtp_settings.password,
            username=smtp_settings.username
        )

    async def __aenter__(self):
        await self.smtp.connect()
        return self
    
    async def __aexit__(self, *args):
        await self.smtp.quit()

    async def send_plaintext(self, subject: str, message_text: str, to_email: str):
        try:
            message = self.create_message(sub=subject, text=message_text, to=to_email)
            await self.smtp.send_message(message)
            logger.info(f"Mail has been sent to '{to_email}'")
        except Exception as e:
            logger.error(e)

    def create_message(self, sub: str, text: str, to: str) -> EmailMessage:
        message = EmailMessage()
        message["From"] = self.from_email
        message["To"] = to
        message["Subject"] = sub
        message.set_content(text)
        return message