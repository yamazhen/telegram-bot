from telegram.ext import ApplicationBuilder
from config import TOKEN

def create_bot():
    if TOKEN is None:
        raise ValueError("Bot token is missing")

    app = ApplicationBuilder().token(TOKEN).build()
    return app
