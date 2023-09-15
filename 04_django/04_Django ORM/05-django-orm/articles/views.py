from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    # DB에서 전체 게시글을 조회 후 받은 전체 게시글 데이터를 변수에 담아
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)