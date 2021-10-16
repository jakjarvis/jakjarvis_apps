from django.forms import ModelForm
from .models import Stock
from .models import Dividend

class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ['ticker', 'memo', 'type', 'volume', 'price', 'date']

class DivForm(ModelForm):
    class Meta:
        model = Dividend
        fields = ['ticker', 'memo', 'type', 'value', 'date']