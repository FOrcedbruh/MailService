from pydantic import BaseModel, EmailStr
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class RunSettings(BaseModel):
    host: str = os.environ.get("HOST")
    port: int = os.environ.get("PORT")


class MailSettings(BaseModel):
    host: str = os.environ.get("SMTP_HOST")
    port: int = os.environ.get("SMTP_PORT")
    from_email: EmailStr = os.environ.get("SMTP_FROM")
    password: str = os.environ.get("SMTP_PASSWORD")
    username: str = os.environ.get("SMTP_NAME")

class BrokerSettings(BaseModel):
    url: str = os.environ.get("BROKER_URL")

class Settings(BaseSettings):
    run: RunSettings = RunSettings()
    smtp: MailSettings = MailSettings()
    broker: BrokerSettings = BrokerSettings()


def get_settings() -> Settings:
    return Settings()