import requests
import csv
import time
import datetime

def getNowDate():
    now    = datetime.datetime.now()
    year   = now.year
    month  = now.month
    day    = now.day
    hour   = now.hour
    minute = now.minute
    nowDate = str(year)+"-"+str(month)+"-"+str(day)+"-"+str(hour)+":"+str(minute)
    return nowDate

def writePrice():
    again = True
    while again :
        now = getNowDate()
        responseFinex = requests.get(urlFinex)
        responseThumb = requests.get(urlThumb)
        usd=responseFinex.text.partition(':')[2].partition(':')[2].partition('}')[0]
        krw=responseThumb.text.partition(':')[2].partition(':')[2].partition('}')[0]
        with open ("price.csv",'a',newline='') as csvfile:
            priceWriter = csv.writer(csvfile, delimiter=',')
            priceWriter.writerow([now,usd,krw])
        time.sleep(60)

def readPrice():
    # again = True
    # while again :
    with open ("price.csv",'r') as csvfile:
        priceReader = csv.reader(csvfile)
        for line in priceReader:
            result=line
        return result