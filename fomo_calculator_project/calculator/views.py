from django.shortcuts import render
from django.http import HttpResponse
from pycoingecko import CoinGeckoAPI
import json
cg = CoinGeckoAPI()

# Create your views here.
def main(requests):
    coin=input("Enter your crypto: ")
    currency=input("Enter your currency: ")
    return HttpResponse(cg.get_price(ids=coin, vs_currencies=currency)[coin][currency])
