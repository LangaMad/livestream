# Generated by Django 5.0.7 on 2024-08-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_games_game_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='game_trailer',
            field=models.FileField(blank=True, null=True, upload_to='games_trailer/', verbose_name='Трейлер игры'),
        ),
    ]
