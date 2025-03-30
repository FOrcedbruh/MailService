from fastapi import FastAPI
import uvicorn
from core.settings import get_settings
from utils import lifespan

settings = get_settings()


app = FastAPI(
    title="Mail service API",
    docs_url="/openapi",
    lifespan=lifespan
)

@app.get("/")
async def index():
    return "Welcome to service!"


if __name__ == "__main__":
    uvicorn.run(app=app, host=str(settings.run.host), port=int(settings.run.port))