from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import NewGame, ScoreSubmit
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
    (
        game,
        player1,
        player2,
        scores1,
        scores2,
        active_player,
        turns_remaining,
    ) = get_values(game_id)
    if request.method == "POST":
        form = ScoreSubmit(request.POST)
        print(form)
        form_values = processFormInput(str(form))
        scores = Scores.objects.get(pk=form_values["scores_id"])
        setattr(
            scores,
            form_values["field"],
            form_values["score"],
        )
        scores.save()
        game.active_player = form_values["active_player"]
        game.turns_remaining = form_values["turns_remaining"]
        game.save()
        (
            game,
            player1,
            player2,
            scores1,
            scores2,
            active_player,
            turns_remaining,
        ) = get_values(game_id)
        print("Form contained: ", form_values)
        print(
            "New value of ",
            form_values["field"],
            " is ",
            getattr(scores, form_values["field"]),
        )
    else:
        form = ScoreSubmit()
    return render(
        request,
        "yahtzee/game.html",
        {
            "game": game,
            "player1": player1,
            "player2": player2,
            "scores1": scores1,
            "scores2": scores2,
            "active_player": active_player,
            "turns_remaining": turns_remaining,
        },
    )


def get_values(game_id):
    game = get_object_or_404(Game, pk=game_id)
    player1 = game.player1
    player2 = game.player2
    scores1 = game.scores1
    scores2 = game.scores2
    active_player = game.active_player
    turns_remaining = game.turns_remaining
    return game, player1, player2, scores1, scores2, active_player, turns_remaining


# For some reason that I haven't had time to look into, when the scores form is submitted, Django recieves the HTML object of the form itself, rather than just the values. This function is a quick and dirty solution for now:
def processFormInput(formHTML):
    form_parameters = {}
    strings = formHTML.split("</tr>\n")
    for string in strings:
        print(string)
        sub_strings = string.split('name="')
        name = sub_strings[1].split('"')[0]
        value = sub_strings[1].split('value="')[1].split('"')[0]
        form_parameters[name] = value
    return form_parameters
