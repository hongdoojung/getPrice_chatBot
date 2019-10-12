import sys
import ChatBotModel
import csv
import getPrice
import time

def proc_rolling(bot, update):
    my3736.sendMessage('데구르르..')
    sound = firecracker()
    my3736.sendMessage(sound)
    my3736.sendMessage('르르..')

def proc_stop(bot, update):
    my3736.sendMessage('3736 봇이 잠듭니다.')
    my3736.stop()

def firecracker():
    return '팡팡!'

def priceRead(bot, update):
    my3736.sendMessage(getPrice.readPrice())
    
def proc_luv(bot, update):
    my3736.sendMessage("나두사랑해")

def keepRead(bot, update):
    my3736.sendMessage("1분마다 마진을 계산")
    while True:
        my3736.sendMessage(getPrice.readPrice())
        ex=getPrice.readPrice()
        time.sleep(60)
        now=getPrice.readPrice()
        usdMargin=float(ex[1])-float(now[1])
        krwMargin=int(ex[2])-int(now[2])
        my3736.sendMessage("usdMargin:"+str(usdMargin)+","+"krwMargin:"+str(krwMargin))


my3736 = ChatBotModel.my3736()
my3736.add_handler('rolling', proc_rolling)
my3736.add_handler('iluvu', proc_luv)
my3736.add_handler('stop', proc_stop)

my3736.add_handler('read', priceRead)
my3736.add_handler('keepRead', keepRead)
my3736.start()