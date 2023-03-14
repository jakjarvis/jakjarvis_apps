# Useful ref: https://stackoverflow.com/questions/69268571/how-to-configure-id-parameters-in-django-rest-framework-apiview

import json

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GameSerializer, ScoresSerializer
from yahtzee.models import Game, Scores
from django.contrib.auth.models import User
from yahtzee.forms import NewGame
from django.http import Http404

# Create your views here.


class RetrieveUpdateGameState(APIView):
    def get(self, request, *args, **kwargs):
        try:
            target_game = Game.objects.get(id=(self.kwargs["pk"]))
        except:
            raise Http404

        ## Outdated code - this could do with refactoring to change filter for just game.player1.username. However this will result in refactor on the front end to expect responses not to be in list form.
        pk = target_game.id
        response = {
            "player1_name": target_game.player1.username,
            "player2_name": target_game.player2.username,
            "scores1_id": target_game.scores1.id,
            "scores2_id": target_game.scores2.id,
            "active_player": target_game.active_player,
            "turns_remaining": target_game.turns_remaining,
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


# class CreateGame(generics.CreateAPIView):
#     print("New Game")

#     serializer_class = GameSerializer

#     def perform_create(self, serializer):
#         if User.objects.filter(user=self.request.player1).exists():
#             player1 = self.request.player1
#         else:
#             player1 = "Guest"

#         if User.objects.filter(user=self.request.player2).exists():
#             player2 = self.request.player2
#         else:
#             player2 = "Guest"

#         serializer.save(player1=player1, player2=player2)


class CreateGame(APIView):
    def post(self, request):

        real_users = [False, False]

        if User.objects.filter(username=request.data["player1"]).exists():
            player1 = User.objects.get(username=request.data["player1"])
            real_users[0] = True
        else:
            player1 = User.objects.get(username="Guest")

        if User.objects.filter(username=request.data["player2"]).exists():
            player2 = User.objects.get(username=request.data["player2"])
            real_users[1] = True
        else:
            player2 = User.objects.get(username="Guest")

        new_game = Game.objects.create_game()
        new_game.player1 = player1
        new_game.player2 = player2
        new_game.save()

        serializer = GameSerializer(Game.objects.get(id=new_game.id))

        response = {"game_id": new_game.id, "user_array": real_users}

        return Response(response)
