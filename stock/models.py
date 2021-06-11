from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    memo = models.TextField(blank=True)
    transactions = [('buy', 'Buy'), ('sel', 'Sell')]
    type = models.CharField(max_length=3, choices=transactions)
    volume = models.FloatField(default=0)
    price = models.FloatField(default=0)
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticker