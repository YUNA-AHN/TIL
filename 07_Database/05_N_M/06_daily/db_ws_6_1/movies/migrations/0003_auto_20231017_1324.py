# Generated by Django 3.2.7 on 2023-10-17 04:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_movie_like_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='like_users',
        ),
        migrations.AddField(
            model_name='movie',
            name='like_users',
            field=models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]