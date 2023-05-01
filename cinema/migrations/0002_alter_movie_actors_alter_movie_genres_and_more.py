# Generated by Django 4.2 on 2023-05-01 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cinema", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(
                blank=True, related_name="movies", to="cinema.actor"
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(
                blank=True, related_name="movies", to="cinema.genre"
            ),
        ),
        migrations.AlterField(
            model_name="moviesession",
            name="cinema_hall",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="movie_sessions",
                to="cinema.cinemahall",
            ),
        ),
        migrations.AlterField(
            model_name="moviesession",
            name="movie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="movie_sessions",
                to="cinema.movie",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
