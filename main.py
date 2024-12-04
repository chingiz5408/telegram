from telegram.ext import Updater,CommandHandler,MessageHandler
from telegram.ext.filters import Filters
import settings
import requests

updater=Updater(token=settings.TELEGRAM_TOKEN)
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Assalomu alekum Wikipediyadan "
                                    "malumot qidiruvchi botga hush "
                                    "kelibsiz.Malumotni '/seach Amir Temur' "
                                    "kabi yozing!")
def search(update, context):
    search_text=" ".join(context.args)
    if len(search_text):
        response = requests.get('https://uz.wikipedia.org/w/api.php',{
            'action':'opensearch',
            'search':search_text,
            'limit':1,
            'namespace':0,
            'format':'json',
        })
        result=response.json()
        link=result[3]
        if len(link):
            update.message.reply_text('Sizning sorovingiz boyicha natija: '+link[0])
        else:
            update.message.reply_text("So'rov bo'yicha natija topilmadi,so'ro'vni to'g'ri yozing!")
    else:
        update.message.reply_text("Siz hech narsa qidirmadingiz!")

dispatcher=updater.dispatcher
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(CommandHandler('search',search))
dispatcher.add_handler(MessageHandler(Filters.all,start))

updater.start_polling()
updater.idle()
