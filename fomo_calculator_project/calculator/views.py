from django.shortcuts import render
from django.http import HttpResponse
from pycoingecko import CoinGeckoAPI
from rest_framework import generics
from .models import MainPage
from .serializers import MainPageSerializer
import json
cg = CoinGeckoAPI()

# Create your views here.
class MainPageView(generics.CreateAPIView):
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer
