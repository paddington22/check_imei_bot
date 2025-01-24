from http import HTTPStatus

from fastapi import APIRouter, Request, Response
from telegram import Update

from core.database.users import Users
from utils.tg_bots import client_ptb
from core.bot import main as clients_main

router = APIRouter(prefix="/telegram_webhooks", tags=["Telegram Webhooks"])


@router.post("/{bot_type}")
async def process_bot_updates(request: Request):
    payload = await request.json()
    update = Update.de_json(payload, client_ptb.bot)
    if not update.effective_message:
        return Response(status_code=HTTPStatus.OK)
    chat_id = update.effective_message.chat_id
    telegram_username = update.effective_message.from_user.username
    bot = client_ptb.bot
    user = await Users.get_or_none(
        telegram_username=telegram_username,
    )

    if not user:
        await bot.send_message(chat_id=chat_id, text="Access denied. User not found, go to registration in API")
    else:
        await clients_main.process_update(user, bot, update)
    return Response(status_code=HTTPStatus.OK)
