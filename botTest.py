import telepot
from pprint import pprint
from telepot.loop import MessageLoop
import telegram
from telegram.ext import Updater, CommandHandler
import sys

def handle(msg):
    pprint(msg)

mytoken='972430101:AAEBh2y65N2fDDCoqmXB-8UWrsh9V5rmWLc'
bot = telepot.Bot(token=mytoken)

bot.getMe()
updates=bot.getUpdates()
for u in updates:
    print(u)