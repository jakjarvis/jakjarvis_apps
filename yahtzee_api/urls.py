from django.urls import path
from . import views

urlpatterns = [
    path("setup", views.CreateGame.as_view()),
    path("game/<int:pk>", views.RetrieveUpdateGameState.as_view()),
    path("scores/<int:pk>", views.RetrieveUpdateScores.as_view()),
]
