from django.forms import ModelForm
from .models import Stock

class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ['ticker', 'memo', 'type', 'volume', 'price', 'date']