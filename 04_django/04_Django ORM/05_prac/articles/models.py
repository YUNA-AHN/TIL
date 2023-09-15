from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'번호 - {id}, 제목 - {self.title}, 내용 - {self.content}, 생성월일 - {self.created_at.month}/{self.created_at.day}'