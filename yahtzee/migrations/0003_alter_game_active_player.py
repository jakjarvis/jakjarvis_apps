# Generated by Django 3.2.16 on 2023-01-27 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yahtzee', '0002_game_active_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='active_player',
            field=models.CharField(default='player2', max_length=10),
        ),
    ]
