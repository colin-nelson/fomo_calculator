from django.db import models

from .utilities import *

# Create your models here.
class MainPage(models.Model):
    coin = models.CharField(max_length=10, default='', unique=False)
    currency = models.CharField(max_length=5, unique=False)
    amount = models.IntegerField(null=False, default=1)
    date = models.DateField(auto_now=False, auto_now_add=False)
    fomo = models.IntegerField(null=True, editable=False)

