from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from config import START_IMAGE_URL

async def start(chat_id, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Help", callback_data="help")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)


    message = await context.bot.send_photo(
        chat_id=chat_id,
        photo=START_IMAGE_URL,
        caption="Welcome to <b>Zhen's Bot</b>",
        parse_mode="HTML",
        reply_markup=reply_markup
    )
    context.user_data["start_message"] = message.message_id
    context.user_data["chat_id"] = chat_id
    context.user_data["current_state"] = "start"

async def help(chat_id, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Back", callback_data="back")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    message = await context.bot.send_message(
        chat_id=chat_id,
        text="You can use the following commands:\n/start - Start the bot\n/help - Get help",
        reply_markup=reply_markup
    )
    context.user_data["help_message"] = message.message_id
    context.user_data["chat_id"] = chat_id
    context.user_data["current_state"] = "help"
