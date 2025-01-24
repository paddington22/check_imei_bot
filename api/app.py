from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.v1.check_imei.routes import router as check_imei_router
from settings.config import settings
from utils.tg_bots import client_ptb



@asynccontextmanager
async def lifespan(_: FastAPI):
    webhook_base_url = settings.BOT_WEBHOOK_URL
    await client_ptb.bot.set_webhook(f"{webhook_base_url}/telegram_webhooks/clients")
    yield
    await client_ptb.bot.delete_webhook()

app = FastAPI(lifespan=lifespan)


app.include_router(
    check_imei_router,
)