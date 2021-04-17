from pycoingecko import CoinGeckoAPI
from datetime import datetime
import json
cg = CoinGeckoAPI()

def getPrice(coin):
    return cg.get_price(ids=coin, vs_currencies='usd')[coin]['usd']

def getHist(coin, date):
    return cg.get_coin_history_by_id(coin, date)['market_data']['current_price']['usd']

def getFOMO(coin, date, buy):
    
    numCoins = buy / getHist(coin, date)
    return getPrice(coin) * numCoins