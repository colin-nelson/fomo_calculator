from rest_framework import serializers
from .models import MainPage

class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = ('id', 'coin', 'currency', 'date', 'amount')

class FomoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = ('coin', 'currency', 'date', 'amount', 'fomo')