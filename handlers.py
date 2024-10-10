from telegram import Message, Update
from telegram.ext import ContextTypes
from messages import start, help
from utils import delete_message

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.callback_query is not None:
        query = update.callback_query
        await query.answer()

        chat_id = context.user_data.get("chat_id")

        if isinstance(query.message, Message):
            if query.data == "help":
                start_message = context.user_data.get("start_message")
                if start_message and chat_id:
                    await delete_message(chat_id, start_message, context)
                await help(chat_id, context)

            elif query.data == "back":
                help_message = context.user_data.get("help_message")
                if help_message and chat_id:
                    await delete_message(chat_id, help_message, context)
                await start(chat_id, context)

async def state_manage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    current_state = context.user_data.get("current_state")

    if current_state == "help":
        help_message = context.user_data.get("help_message")
        if help_message:
            await delete_message(chat_id, help_message, context)
            await help(chat_id, context)
    elif current_state == "start":
        start_message = context.user_data.get("start_message")
        if start_message:
            await delete_message(chat_id, start_message, context)
            await start(chat_id, context)
    else:
        await start(chat_id, context)
