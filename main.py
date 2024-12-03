from telegram.bot import Bot
from telegram.ext import Updater,Dispatcher,CommandHandler,CallbackContext
from telegram.update import Update
import settings

updater=Updater(token=settings.TELEGRAM_TOKEN)
# def start(update:Update,context:CallbackContext):
#     update.message.reply_text('salom')
def start(update, context):
    print(update.message.chat_id)
    print(update.effective_chat.id)
    context.bot.send_message(chat_id=update.message.chat_id, text="Salom, Telegram botga xush kelibsiz!")

dispatcher=updater.dispatcher
dispatcher.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()
