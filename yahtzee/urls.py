from django.urls import path, include
from yahtzee import views

urlpatterns = [
    path("version", views.version, name="yahtzee_version"),
    path("setup", views.setup, name="yahtzee_setup"),
    path("<int:game_id>", views.game, name="yahtzee_game"),
    # API
    path("api/", include("yahtzee_api.urls")),
]
