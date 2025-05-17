from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hello! I am your bot.')

updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()