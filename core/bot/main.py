import json

from telegram import Update

from core.database.users import Users
from utils.tg_bots import client_ptb
from utils.imei_validator import is_valid_imei
from utils.request import get_request

from settings.config import settings


async def process_update(user: Users, bot: client_ptb.bot, update: Update):
    chat_id = update.message.chat_id
    message = update.message.text
    state = user.telegram_context.get("state")

    if message == "/start":
        user.telegram_context["state"] = "active"
        await user.save()
        await bot.send_message(chat_id=chat_id, text="input IMEI for verify")

    if state == "active":
        try:
            is_valid_imei(message)
            response = get_request(token=settings.API_TOKEN, device_id=message)
            if response.status_code == 200:
                user.telegram_context["state"] = "waiting"
                await user.save()
                msg = ""
                for k,v in response.json()["properties"].items():
                    msg += f"{k}: {v}\\n"
                msg += "send '/start' for check again"
                await bot.send_message(chat_id=chat_id, text=msg)
            else:
                await bot.send_message(chat_id=chat_id, text=f"Error! Status code: {response.status_code}")
        except ValueError:
            await bot.send_message(chat_id=chat_id, text="Invalid IMEI, try again")
