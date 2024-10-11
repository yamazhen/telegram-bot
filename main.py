from telegram.ext import CallbackQueryHandler, CommandHandler, MessageHandler, filters
from bot import create_bot
from handlers import handle_registration, start_command, system_management
from messages import start

if __name__ == "__main__":
    app = create_bot()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.CONTACT, handle_registration))
    app.add_handler(MessageHandler((filters.TEXT & ~filters.COMMAND), system_management))
    app.add_handler(CallbackQueryHandler(system_management))

    print("Bot is running")
    app.run_polling()
