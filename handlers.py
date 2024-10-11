from telegram import Message, Update
from telegram.ext import ContextTypes
from messages import register, registersuccess, start, help
from utils import delete_message, save_to_excel

async def handle_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data is None:
        context.user_data = {}

    chat_id = context.user_data.get("chat_id")

    if update.message:
        if update.message.contact:
            register_message = context.user_data.get("register_message")
            if register_message and chat_id:
                await delete_message(chat_id, register_message, context)
            phone_number = update.message.contact.phone_number
            save_to_excel(phone_number)
            await registersuccess(chat_id, context)
            return

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data is None:
        context.user_data = {}

    chat_id = context.user_data.get("chat_id")
    get_userdata = context.user_data.get

    if update.message:
        button_text = update.message.text
        if button_text == "Back":
            help_message = get_userdata("help_message")
            register_message = get_userdata("register_message")
            registersuccess_message = get_userdata("registersuccess_message")
            if register_message and chat_id:
                await delete_message(chat_id, register_message, context)
            elif registersuccess_message and chat_id:
                await delete_message(chat_id, registersuccess_message, context)
            elif help_message and chat_id:
                await delete_message(chat_id, help_message, context)
            await start(chat_id, context)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data is None:
        context.user_data = {}
    get_userdata = context.user_data.get

    if update.callback_query is not None:
        query = update.callback_query
        await query.answer()

        chat_id = context.user_data.get("chat_id")

        if isinstance(query.message, Message):
            if query.data == "help":
                start_message = get_userdata("start_message")
                if start_message and chat_id:
                    await delete_message(chat_id, start_message, context)
                await help(chat_id, context)
            elif query.data == "register":
                start_message = get_userdata("start_message")
                if start_message and chat_id:
                    await delete_message(chat_id, start_message, context)
                await register(chat_id, context)


async def system_management(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data is None:
        context.user_data = {}
    if not update.effective_chat:
        return
    chat_id = update.effective_chat.id
    current_state = context.user_data.get("current_state")
    get_userdata = context.user_data.get

    if update.callback_query:
        await button_callback(update, context)
    elif update.message:
        await handle_message(update, context)

    if current_state == "help":
        help_message = get_userdata("help_message") 
        if help_message:
            await delete_message(chat_id, help_message, context)
            await help(chat_id, context)
    elif current_state == "start":
        start_message = get_userdata("start_message")
        if start_message:
            await delete_message(chat_id, start_message, context)
            await start(chat_id, context)
    elif current_state == "register":
        register_message = get_userdata("register_message")
        if register_message:
            await delete_message(chat_id, register_message, context)
            await register(chat_id, context)
    elif current_state == "registersuccess":
        registersuccess_message = get_userdata("registersuccess_message")
        if registersuccess_message:
            await delete_message(chat_id, registersuccess_message, context)
            await registersuccess(chat_id, context)
    else:
        await start(chat_id, context)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data is None:
        context.user_data = {}
    get_userdata = context.user_data.get

    chat_id = context.user_data.get("chat_id")
    help_message = get_userdata("help_message")
    register_message = get_userdata("register_message")
    registersuccess_message = get_userdata("registersuccess_message")
    if register_message and chat_id:
        await delete_message(chat_id, register_message, context)
    elif registersuccess_message and chat_id:
            await delete_message(chat_id, registersuccess_message, context)
    elif help_message and chat_id:
            await delete_message(chat_id, help_message, context)

    await start(update.effective_chat.id, context)
