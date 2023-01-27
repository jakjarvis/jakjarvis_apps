from django import forms
from yahtzee.models import Game, Scores


class NewGame(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["player1", "player2"]


# class SubmitScore(forms.ModelForm):
#     class Meta:
#         model = Scores
#         fields = [
#             "ones",
#             "twos",
#             "threes",
#             "fours",
#             "fives",
#             "sixes",
#             "three_kind",
#             "four_kind",
#             "full_house",
#             "short_straight",
#             "long_straight",
#             "yahtzee",
#             "chance",
#         ]


class ScoreSubmit(forms.Form):
    scores_id = forms.IntegerField()
    score = forms.IntegerField()
    field = forms.CharField(max_length=30)
    active_player = forms.CharField(max_length=10)
    turns_remaining = forms.IntegerField()
