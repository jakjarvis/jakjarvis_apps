from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import NewGame
from .models import Scores, Game


def setup(request):
    if request.method == "POST":
        form = NewGame(request.POST)
        new_game = form.save(commit=False)
        new_game.scores1 = Scores.objects.create_scores()
        new_game.scores2 = Scores.objects.create_scores()
        new_game.save()
        return HttpResponseRedirect("/yahtzee/" + str(new_game.id))
    else:
        form = NewGame()
    return render(request, "yahtzee/setup.html", {"form": form})


def game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    scores1 = game.scores1
    scores2 = game.scores2
    return render(
        request,
        "yahtzee/game.html",
        {"game": game, "scores1": scores1, "scores2": scores2},
    )
