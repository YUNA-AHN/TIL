from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    address = models.TextField()
    phone_number = models.TextField()