from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Message, Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes
from dotenv import load_dotenv
from util import reply_text
import os

load_dotenv()

token = os.getenv("TELEGRAM_KEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Help", callback_data="help")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.effective_user is not None:
        await reply_text(update, f"Hello {update.effective_user.first_name}! I am your bot.", 2,
                                        reply_markup = reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.callback_query is not None:
        query = update.callback_query
        await query.answer()
   
        if isinstance(query.message, Message):
            if query.data == "help":
                await reply_text(update, "You can use the following commands:\n/start - Start the bot\n/help - Get help", 1)
    
if __name__ == "__main__":
    TOKEN = token 

    if TOKEN is None:
        raise ValueError("Bot token is missing")
    
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))

    print("Bot is running...")
    app.run_polling()
