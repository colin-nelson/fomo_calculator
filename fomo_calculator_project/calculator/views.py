from django.shortcuts import render
from django.http import HttpResponse
from pycoingecko import CoinGeckoAPI
from rest_framework import generics, status
from .models import MainPage
from .serializers import MainPageSerializer, FomoSerializer
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .utilities import *
import datetime
cg = CoinGeckoAPI()


# Create your views here.
class MainPageView(generics.CreateAPIView):
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer

class FomoView(APIView):
    serializer_class = FomoSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            coin = serializer.data.get('coin')
            currency = serializer.data.get('currency')
            date = serializer.data.get('date')
            amount = serializer.data.get('amount')
            newDate = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%d-%m-%Y')
            fomo = getFOMO(coin, newDate, amount)

            page = MainPage(coin=coin, currency=currency, date=date, amount=amount, fomo=fomo)
            page.save()

            return Response(FomoSerializer(page).data, status=status.HTTP_201_CREATED)
        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)