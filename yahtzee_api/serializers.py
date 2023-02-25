from rest_framework import serializers
from yahtzee.models import Game, Scores


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            "player1",
            "player2",
            "scores1",
            "scores2",
            "active_player",
            "turns_remaining",
            "completed",
        ]


class ScoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scores
        fields = [
            "ones",
            "twos",
            "threes",
            "fours",
            "fives",
            "sixes",
            "three_kind",
            "four_kind",
            "full_house",
            "short_straight",
            "long_straight",
            "yahtzee",
            "chance",
            "top_score",
            "bonus",
            "top_total",
            "bottom_total",
            "grand_total",
        ]