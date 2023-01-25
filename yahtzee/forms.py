from django.forms import ModelForm
from yahtzee.models import Game


class NewGame(ModelForm):
    class Meta:
        model = Game
        fields = ["player1", "player2"]
