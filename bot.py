from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config import API_TOKEN

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to the Trading Bot!")

def main():
    updater = Updater(API_TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
