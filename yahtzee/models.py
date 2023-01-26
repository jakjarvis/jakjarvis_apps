from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ScoresManager(models.Manager):
    def create_scores(self):
        scores = self.create()
        return scores


class Scores(models.Model):
    ones = models.SmallIntegerField(null=True)
    twos = models.SmallIntegerField(null=True)
    threes = models.SmallIntegerField(null=True)
    fours = models.SmallIntegerField(null=True)
    fives = models.SmallIntegerField(null=True)
    sixes = models.SmallIntegerField(null=True)

    three_kind = models.SmallIntegerField(null=True)
    four_kind = models.SmallIntegerField(null=True)
    full_house = models.SmallIntegerField(null=True)
    short_straight = models.SmallIntegerField(null=True)
    long_straight = models.SmallIntegerField(null=True)
    yahtzee = models.SmallIntegerField(null=True)
    chance = models.SmallIntegerField(null=True)

    top_score = models.SmallIntegerField(null=True)
    bonus = models.SmallIntegerField(null=True)
    top_total = models.SmallIntegerField(null=True)
    bottom_total = models.SmallIntegerField(null=True)
    grand_total = models.SmallIntegerField(null=True)

    objects = ScoresManager()


class Game(models.Model):
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="player1")
    player2 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="player2", blank=True
    )
    scores1 = models.ForeignKey(
        Scores, on_delete=models.CASCADE, related_name="player1scores"
    )
    scores2 = models.ForeignKey(
        Scores, on_delete=models.CASCADE, related_name="player2scores", blank=True
    )
    completed = models.BooleanField(default=False)