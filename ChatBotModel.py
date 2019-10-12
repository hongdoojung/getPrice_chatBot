import telegram
from telegram.ext import Updater, CommandHandler

class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = 937210580
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id = self.id, text=text)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

mytoken='972430101:AAEBh2y65N2fDDCoqmXB-8UWrsh9V5rmWLc'
class my3736(TelegramBot):
    def __init__(self):
        self.token = mytoken
        TelegramBot.__init__(self, 'my3736', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage('my3736 봇이 잠에서 깨어납니다.')
        self.updater.start_polling()
        self.updater.idle()