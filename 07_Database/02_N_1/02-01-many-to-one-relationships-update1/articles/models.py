from django.db import models
from accounts.models import User
from django.contrib.auth import get_user_model
# Create your models here.


class Article(models.Model):
    author = models.ForeignKey(
        # , on_delete=models.SET_NULL, null=True
        get_user_model(), on_delete=models.CASCADE,
        related_name="writtens"
    )
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
