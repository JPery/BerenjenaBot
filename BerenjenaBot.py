from telegram import Updater
import telegram
import random

TOKEN = ""
bot = telegram.Bot(TOKEN)
updater = Updater(TOKEN)
updater.start_polling()
dispatcher = updater.dispatcher

nmensaje = random.randint(10,50)
print("Numero de mensajes", nmensaje)
contador = 1

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="\xF0\x9F\x98\x8F\xF0\x9F\x8D\x86")

dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addTelegramCommandHandler('berenjen', start)
dispatcher.addTelegramCommandHandler('berenjeno', start)

def echo(bot, update):
    global nmensaje
    global contador
    if contador==nmensaje:
       bot.sendMessage(chat_id=update.message.chat_id, text="\xF0\x9F\x98\x8F\xF0\x9F\x8D\x86")
       nmensaje = random.randint(10,50)
       contador = 1
       print("Numero de mensajes", nmensaje)

    else:
        user_id = update.message.from_user.id
        nombre = update.message.from_user.username
        print (contador, user_id, nombre)
        contador += 1

dispatcher.addTelegramMessageHandler(echo)
