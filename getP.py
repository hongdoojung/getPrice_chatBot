{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "urlFinex = \"https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC&tsyms=USD&e=Bitfinex&extraParams=coin-2014023736\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "urlThumb = \"https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC&tsyms=KRW&e=Bithumb&extraParams=coin-2014023736\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "responseFinex = requests.get(urlFinex)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "responseThumb = requests.get(urlThumb)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "200"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "responseFinex.status_code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "200"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "responseThumb.status_code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'{\"BTC\":{\"USD\":8347.95}}'"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "responseFinex.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'{\"BTC\":{\"KRW\":9883000}}'"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "responseThumb.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'9883000'"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "krw"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [],
   "source": [
    "usd=responseFinex.text.partition(':')[2].partition(':')[2].partition('}')[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [],
   "source": [
    "krw=responseThumb.text.partition(':')[2].partition(':')[2].partition('}')[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "metadata": {},
   "outputs": [],
   "source": [
    "def getNowDate():\n",
    "\n",
    "    now    = datetime.datetime.now()\n",
    "\n",
    "    year   = now.year\n",
    "\n",
    "    month  = now.month\n",
    "\n",
    "    day    = now.day\n",
    "\n",
    "    hour   = now.hour\n",
    "\n",
    "    minute = now.minute\n",
    "    \n",
    "    nowDate = str(year)+\"-\"+str(month)+\"-\"+str(day)+\"-\"+str(hour)+\":\"+str(minute)\n",
    "    \n",
    "    return nowDate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2019-10-12-14:49'"
      ]
     },
     "execution_count": 186,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "getNowDate()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Sat Oct 12 14:20:58 2019', '8353.8', '9890000']"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[now,usd,krw]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "while True :\n",
    "    now = getNowDate()\n",
    "    responseFinex = requests.get(urlFinex)\n",
    "    responseThumb = requests.get(urlThumb)\n",
    "    usd=responseFinex.text.partition(':')[2].partition(':')[2].partition('}')[0]\n",
    "    krw=responseThumb.text.partition(':')[2].partition(':')[2].partition('}')[0]\n",
    "    with open (\"price.csv\",'a',newline='') as csvfile:\n",
    "        pricewriter = csv.writer(csvfile, delimiter=',')\n",
    "        pricewriter.writerow([now,usd,krw])\n",
    "    time.sleep(60)\n",
    "    break\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "with open (\"price.csv\",'r') as csvfile:\n",
    "        priceReader = csv.reader(csvfile)\n",
    "        for line in priceReader:\n",
    "            result=line\n",
    "        result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['2019-10-12-17:59', '8371.7', '9909000']\n"
     ]
    }
   ],
   "source": [
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
