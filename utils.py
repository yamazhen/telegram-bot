from telegram.ext import ContextTypes

async def delete_message(chat_id: int, message_id: int, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
