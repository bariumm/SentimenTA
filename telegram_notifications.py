import os
from dotenv import load_dotenv
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')
application = Application.builder().token("TOKEN").build()

#class TelegramNotifications:
def __init__():
    application.run_polling(allowed_updates=Update.ALL_TYPES)
    send_message()
    

def send_message(message: str) -> None:
    """Send a message to the chat."""
    # Send the message to the chat.
    application.send_message(chat_id, message, parse_mode=ParseMode.MARKDOWN)