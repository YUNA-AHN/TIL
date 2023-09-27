from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 공백을 허용, 안해주면 글 쓸때마다 사진 넣기
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
