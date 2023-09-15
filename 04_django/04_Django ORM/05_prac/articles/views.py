from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
# Read : 전체 게시글 조회
def index(request):
    articles = Article.objects.all() # 게시글 정보를 모두 가져온다
    context = {
        'articles' : articles
    }
    return render(request, "articles/index.html", context)

# Delete : 해당 게시글 삭제
def delete(request,pk):
    # 1. pk를 가지고 있는 게시글 조회
    article = Article.objects.get(pk=pk)
    # 2. 게시글 삭제 delete
    article.delete()
    
    return redirect("articles:index")

# # 게시글을 생성하는 폼을 렌더해준 페이지를 반환하는 함수
# def make(request):
#     return render(request, "articles/new.html")

# 데이터로 게시글을 생성
def create(request):
    if request.method == "POST":
        # 게시글 제목
        title = request.POST.get("title")
        # 게시글 내용
        content = request.POST.get("content")
        
        # 게시글 인스턴스를 생성
        article = Article()
        article.title = title
        article.content = content
        
        # 저장 (생성)
        article.save()
        
        # 메인 페이지
        return redirect("articles:index")
    else: # get 폼을 랜더링해서 전달
        return render(request, "articles/new.html")