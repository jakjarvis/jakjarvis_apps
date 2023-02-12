# Useful ref: https://stackoverflow.com/questions/69268571/how-to-configure-id-parameters-in-django-rest-framework-apiview

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GameSerializer, ScoresSerializer
from yahtzee.models import Game, Scores
from django.contrib.auth.models import User

# Create your views here.


class RetrieveUpdateGameState(APIView):
    def get(self, request, *args, **kwargs):
        try:
            pk = self.kwargs["pk"]
        except:
            return Response("No id")
        response = {
            "player1:name": (
                game.player1.username for game in Game.objects.filter(id=pk)
            ),
            "player2_name": (
                game.player2.username for game in Game.objects.filter(id=pk)
            ),
            "scores1_id": (game.scores1.id for game in Game.objects.filter(id=pk)),
            "scores2_id": (game.scores2.id for game in Game.objects.filter(id=pk)),
            "active_player": (
                game.active_player for game in Game.objects.filter(id=pk)
            ),
            "turns_remaining": (
                game.turns_remaining for game in Game.objects.filter(id=pk)
            ),
        }
        return Response(response)

    def put(self, request, *args, **kwargs):
        try:
            pk = self.kwargs["pk"]
        except:
            return Response("No id")
        game = Game.objects.get(id=pk)
        data = request.data

        if data.get("active_player") is not None:
            game.active_player = data.get("active_player")
        if data.get("turns_remaining") is not None:
            game.turns_remaining = data.get("turns_remaining")
        game.save()
        serializer = GameSerializer(game)

        return Response(serializer.data)


class RetrieveUpdateScores(generics.RetrieveUpdateAPIView):
    serializer_class = ScoresSerializer

    def get_queryset(self):
        return Scores.objects.all()

    def perform_update(self, serializer):
        serializer.save()
