import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


bot_token = '6216739188:AAGI1LRLGG_CSeqCHgdGaq8lYkZr31omDTY'
bot = telegram.Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот.")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()