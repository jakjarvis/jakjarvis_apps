# Generated by Django 3.2.16 on 2023-01-27 10:36

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yahtzee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='active_player',
            field=models.IntegerField(default=1, verbose_name=django.contrib.auth.models.User),
        ),
    ]
