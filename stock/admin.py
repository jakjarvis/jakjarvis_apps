from django.contrib import admin
from .models import Stock
from .models import Dividend


admin.site.register(Stock)
admin.site.register(Dividend)

