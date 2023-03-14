from django.urls import path
from . import views

urlpatterns = [
    path("setup", views.CreateGame.as_view(), name="create-game"),
    path(
        "game/<int:pk>", views.RetrieveUpdateGameState.as_view(), name="retrieve-game"
    ),
    path(
        "scores/<int:pk>", views.RetrieveUpdateScores.as_view(), name="retrieve-scores"
    ),
]
