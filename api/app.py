from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from tortoise import Tortoise

from settings.config import TORTOISE_CONFIG

from api.v1.check_imei.routes import router as check_imei_router
from api.v1.auth.routes import router as auth_router
from api.bot.routes import router as bot_router
from settings.config import settings
from utils.tg_bots import client_ptb


@asynccontextmanager
async def lifespan(_: FastAPI):
    webhook_base_url = settings.BOT_WEBHOOK_URL
    await Tortoise.init(config=TORTOISE_CONFIG)
    await client_ptb.bot.set_webhook(f"{webhook_base_url}/telegram_webhooks/clients")
    yield
    await client_ptb.bot.delete_webhook()
    await Tortoise.close_connections()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(check_imei_router)
app.include_router(auth_router)
app.include_router(bot_router)
