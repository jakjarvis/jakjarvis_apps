from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from yahtzee.models import Game, Scores
import json

# Create your tests here.
class RetrieveUpdateGameStateTests(TestCase):
    def setUp(self):
        User.objects.create_user(username="Guest")
        Game.objects.create_game()

    def test_get_valid_game(self):
        # should return the game state object
        game = Game.objects.get(id=1)
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
        # should return 404
        game_id = Game.objects.last().id + 1
        response = self.client.get(reverse("retrieve-game", kwargs={"pk": game_id}))
        self.assertEqual(response.status_code, 404)

    def test_get_game_without_id(self):
        # should return 404
        response = self.client.get("/game")
        self.assertEqual(response.status_code, 404)

    def test_put_valid_game_state(self):
        # should update the active player and turns remaining and return them to the requester
        new_game = Game.objects.create_game()
        response = self.client.put(
            reverse("retrieve-game", kwargs={"pk": new_game.id}),
            {"active_player": "player2", "turns_remaining": 10},
            content_type="application/json",
            HTTP_ACCEPT="application/json",
        )
        updated_game = Game.objects.get(id=new_game.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_game.turns_remaining, 10)
        self.assertDictEqual(
            json.loads(response.content.decode("utf-8")),
            {
                "player1_name": updated_game.player1.username,
                "player2_name": updated_game.player2.username,
                "scores1_id": updated_game.scores1.id,
                "scores2_id": updated_game.scores2.id,
                "active_player": updated_game.active_player,
                "turns_remaining": updated_game.turns_remaining,
            },
        )

    def test_put_invalid_game_state(self):
        # if any invalid information is sent, it should return a 400 and not update any information
        new_game = Game.objects.create_game()
        response = self.client.put(
            reverse("retrieve-game", kwargs={"pk": new_game.id}),
            {"invalid_key": "value", "turns_remaining": 5},
            content_type="application/json",
            HTTP_ACCEPT="application/json",
        )
        updated_game = Game.objects.get(id=new_game.id)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(updated_game.turns_remaining, 26)


class RetrieveUpdateScoresTests(TestCase):
    def setUp(self):
        Scores.objects.create_scores()

    def test_get_valid_scores(self):
        # should return the scores object
        scores = Scores.objects.get(id=1)
        response = self.client.get(reverse("retrieve-scores", kwargs={"pk": scores.id}))
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            json.loads(response.content.decode("utf-8")),
            {
                "ones": scores.ones,
                "twos": scores.twos,
                "threes": scores.threes,
                "fours": scores.fours,
                "fives": scores.fives,
                "sixes": scores.sixes,
                "three_kind": scores.three_kind,
                "four_kind": scores.four_kind,
                "full_house": scores.full_house,
                "short_straight": scores.short_straight,
                "long_straight": scores.long_straight,
                "yahtzee": scores.yahtzee,
                "chance": scores.chance,
                "top_score": scores.top_score,
                "bonus": scores.bonus,
                "top_total": scores.top_total,
                "bottom_total": scores.bottom_total,
                "grand_total": scores.grand_total,
            },
        )

    def test_get_invalid_scores(self):
        # should return 404
        scores_id = Scores.objects.last().id + 1
        response = self.client.get(reverse("retrieve-scores", kwargs={"pk": scores_id}))
        self.assertEqual(response.status_code, 404)

    def test_get_scores_without_id(self):
        # should return 404
        response = self.client.get("/scores")
        self.assertEqual(response.status_code, 404)

    def test_put_valid_scores(self):
        new_scores = Scores.objects.create_scores()
        put_score = {"ones": 5}
        response = self.client.put(
            reverse("retrieve-scores", kwargs={"pk": new_scores.id}),
            put_score,
            content_type="application/json",
            HTTP_ACCEPT="application/json",
        )
        updated_scores = Scores.objects.get(id=new_scores.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_scores.ones, 5)
        self.assertDictEqual(
            json.loads(response.content.decode("utf-8")),
            {
                "ones": updated_scores.ones,
                "twos": updated_scores.twos,
                "threes": updated_scores.threes,
                "fours": updated_scores.fours,
                "fives": updated_scores.fives,
                "sixes": updated_scores.sixes,
                "three_kind": updated_scores.three_kind,
                "four_kind": updated_scores.four_kind,
                "full_house": updated_scores.full_house,
                "short_straight": updated_scores.short_straight,
                "long_straight": updated_scores.long_straight,
                "yahtzee": updated_scores.yahtzee,
                "chance": updated_scores.chance,
                "top_score": updated_scores.top_score,
                "bonus": updated_scores.bonus,
                "top_total": updated_scores.top_total,
                "bottom_total": updated_scores.bottom_total,
                "grand_total": updated_scores.grand_total,
            },
        )

    def test_put_invalid_scores(self):
        new_scores = Scores.objects.create_scores()
        put_score = {"sevens": 7}
        try:
            response = self.client.put(
                reverse("retrieve-scores", kwargs={"pk": new_scores.id}),
                put_score,
                content_type="application/json",
                HTTP_ACCEPT="application/json",
            )
        except:
            self.assertRaises(ValidationError)


class CreateGameTests(TestCase):
    def setUp(self):
        User.objects.create_user(username="Guest")

    def test_create_new_game(self):
        player1 = "TestUser"
        player2 = "AnotherUser"
        User.objects.create_user(username=player1)
        response = self.client.post(
            reverse("create-game"),
            {"player1": player1, "player2": player2},
            content_type="application/json",
            HTTP_ACCEPT="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(response.content.decode("utf-8")),
            {"game_id": 1, "user_array": [True, False]},
        )
