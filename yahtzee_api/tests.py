from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from yahtzee.models import Game
import json

# Create your tests here.
class RetrieveUpdateGameStateTests(TestCase):
    def setUp(self):
        User.objects.create_user(username="Guest")
        Game.objects.create_game()

    def test_get_valid_game(self):
        game = Game.objects.first()
        response = self.client.get(reverse("retrieve-game", kwargs={"pk": game.id}))
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            json.loads(response.content.decode("utf-8")),
            {
                "player1_name": game.player1.username,
                "player2_name": game.player2.username,
                "scores1_id": game.scores1.id,
                "scores2_id": game.scores2.id,
                "active_player": game.active_player,
                "turns_remaining": game.turns_remaining,
            },
        )

    def test_get_invalid_game(self):
        game_id = Game.objects.last().id + 1
        response = self.client.get(reverse("retrieve-game", kwargs={"pk": game_id}))
        self.assertEqual(response.status_code, 404)

    def test_get_game_without_id(self):
        response = self.client.get("/game")
        self.assertEqual(response.status_code, 404)
