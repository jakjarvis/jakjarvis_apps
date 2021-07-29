from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Advent(models.Model):
    year = models.IntegerField(default=2015)
    day = models.IntegerField(default=1)
    memo = models.TextField(blank=True)

    def __str__(self):
        return '{0}; Day {1}; Part{2}'.format(self.year, self.day, self.part)