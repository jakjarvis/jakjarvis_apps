from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    memo = models.TextField(blank=True)
    transactions = [('buy', 'Buy'), ('sel', 'Sell')]
    type = models.CharField(max_length=3, choices=transactions)
    volume = models.FloatField(default=0)
    price = models.FloatField(default=0)
    currency = models.CharField(default='EUR', max_length=15)
    currency_con = models.FloatField(default=1)
    date = models.DateField(null=True, default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticker

class Dividend(models.Model):
    ticker = models.CharField(max_length=10)
    memo = models.TextField(blank=True)
    types = [('divd', 'Dividend'), ('right', 'Rights Sale')]
    type = models.CharField(max_length=5, choices=types)
    value = models.FloatField(default=0)
    currency = models.CharField(default='EUR', max_length=15)
    currency_con = models.FloatField(default=1)
    date = models.DateField(null=True, default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticker