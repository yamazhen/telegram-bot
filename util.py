from typing import Optional
from telegram import Update, Message, InlineKeyboardMarkup

async def reply_text(update: Update, message, method, reply_markup: Optional[InlineKeyboardMarkup]=None):
    if method == 1 and update.callback_query and isinstance(update.callback_query.message, Message):
        await update.callback_query.message.reply_text(message)
    if method == 2 and update.message is not None:
        await update.message.reply_text(message, reply_markup=reply_markup)
