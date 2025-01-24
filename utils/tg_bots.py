from telegram.ext import ApplicationBuilder

from settings.config import settings

client_ptb = ApplicationBuilder().updater(None).token(settings.CLIENTS_BOT_TOKEN).build()
