from django.shortcuts import render
from django.http import HttpResponse
from pycoingecko import CoinGeckoAPI
import json
cg = CoinGeckoAPI()

# Create your views here.
def main(requests):
    coin=input("Enter your crypto: ")
    date=input("Enter your date: ")
    return HttpResponse(getFOMO(coin, date))

def getPrice(coin):
    return cg.get_price(ids=coin, vs_currencies='usd')[coin]['usd']

def getHist(coin, date):
    return cg.get_coin_history_by_id(coin, date)['market_data']['current_price']['usd']

def getFOMO(coin, date):
    buy = float(input("How much did you buy? "))
    if getHist(coin, date) > buy:
        numCoins = getHist(coin, date) / buy
    else:
        numCoins = buy / getHist(coin, date)

    return (getPrice(coin) - getHist(coin, date)) * numCoins
