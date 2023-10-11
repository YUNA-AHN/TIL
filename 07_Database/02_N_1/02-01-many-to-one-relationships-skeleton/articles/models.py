from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               related_name='writtens')
                            #    , on_delete=models.SET_NULL, null= True)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete= models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
