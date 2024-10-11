from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from config import START_IMAGE_URL

async def start(chat_id, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Help", callback_data="help")],
        [InlineKeyboardButton("Register", callback_data="register")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    message = await context.bot.send_photo(
        chat_id=chat_id,
        photo=START_IMAGE_URL,
        caption="Welcome to <b>Zhen's Bot</b>",
        parse_mode="HTML",
        reply_markup=reply_markup
    )

    user_context = context.user_data

    if user_context is None:
        user_context = {}

    user_context["start_message"] = message.message_id
    user_context["chat_id"] = chat_id
    user_context["current_state"] = "start"

async def help(chat_id, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("Back")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

    message = await context.bot.send_message(
        chat_id=chat_id,
        text="You can use the following commands:\n/start - Start the bot\n/help - Get help",
        reply_markup=reply_markup
    )

    user_context = context.user_data

    if user_context is None:
        user_context = {}

    user_context["help_message"] = message.message_id
    user_context["chat_id"] = chat_id
    user_context["current_state"] = "help"

async def register(chat_id, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("Register Phone", request_contact=True)],
        [KeyboardButton("Back")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

    message = await context.bot.send_message(
        chat_id=chat_id,
        text="Please tap on <b>[Register Phone]</b>",
        reply_markup=reply_markup,
        parse_mode="HTML"
    )

    user_context = context.user_data

    if user_context is None:
        user_context = {}

    user_context["register_message"] = message.message_id
    user_context["chat_id"] = chat_id
    user_context["current_state"] = "register"

async def registersuccess(chat_id, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("Back")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    message = await context.bot.send_message(
        chat_id=chat_id,
        text="Phone number saved",
        reply_markup=reply_markup,
    )
    user_context = context.user_data

    if user_context is None:
        user_context = {}

    user_context["registersuccess_message"] = message.message_id
    user_context["chat_id"] = chat_id
    user_context["current_state"] = "registersuccess"
