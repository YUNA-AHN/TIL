from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 데이터 처음 생성할 때 현재 일자로
    created_at = models.DateTimeField(auto_now_add = True)
    # 저장(갱신) 할때마자 현재 일자로
    updated_at = models.DateTimeField(auto_now = True)