from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.exceptions import ValidationError

class Wort(models.Model):
    wort = models.CharField(max_length=50)
    memo = models.TextField(blank=True)
    arten_list = [
        ('nomen', 'Nomen'),
        ('pronomen', 'Pronomen'),
        ('verb', 'Verb'),
        ('adjectiv', 'Adjectiv'),
        ('adverb', 'Adverb'),
        ('praeposition', 'Präposition'),
        ('konjunktion', 'Konjunktion'),
        ('zwischenruf', 'Zwischenruf')
    ]
    art = models.CharField(max_length=12, choices=arten_list, default='nomen')
    artikel_list = [
        ('der', 'Der'),
        ('die', 'Die'),
        ('das', 'Das')
    ]
    artikel = models.CharField(max_length=3, blank=True)
    englisch = models.CharField(max_length=50)
    quelle = models.CharField(max_length=50)
    referenz = models.TextField(blank=True)
    wurzel1 = models.CharField(max_length=50, blank=True)
    wurzel2 = models.CharField(max_length=50, blank=True)
    wurzel3 = models.CharField(max_length=50, blank=True)
    wurzel4 = models.CharField(max_length=50, blank=True)
    wurzel5 = models.CharField(max_length=50, blank=True)
    date = models.DateField(null=True, default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.wort