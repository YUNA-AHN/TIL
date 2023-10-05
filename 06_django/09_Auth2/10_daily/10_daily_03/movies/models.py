from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=30)
    comment = models.TextField()
    