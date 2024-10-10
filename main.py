from telegram.ext import CallbackQueryHandler, CommandHandler, MessageHandler, filters
from bot import create_bot
from handlers import state_manage, button_callback

if __name__ == "__main__":
    app = create_bot()

    app.add_handler(CommandHandler("start", state_manage))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, state_manage))
    app.add_handler(CallbackQueryHandler(button_callback))

    print("Bot is running")
    app.run_polling()
