from django.urls import path
from yahtzee import views

urlpatterns = [
    path("setup", views.setup, name="yahtzee_setup"),
    path("<int:game_id>", views.game, name="yahtzee_game"),
]
