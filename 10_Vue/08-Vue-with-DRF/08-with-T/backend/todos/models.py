from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.TextField()
    completed = models.BooleanField(default=False)