from django.contrib import admin

from .models import Game
from .models import Scores


admin.site.register(Game)
admin.site.register(Scores)
