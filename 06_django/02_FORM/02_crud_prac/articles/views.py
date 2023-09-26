import re
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    articles = get_list_or_404(Article)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # objects 매니저를 사용해서 조회
    # 내가 조회하려는 글이 없는 경우 404
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)

# # 사용자의 입력을 받기
# def new(request):
#     return render(request, 'articles/new.html')

# 사용자의 입력을 받아서 생성
def create(request):
    if request.method == 'POST':
        # 사용자로부터 받아온 form 인스턴스 생성
        form = ArticleForm(data=request.POST)
        
        # 사용자가 보낸 데이터가 유효하다면
        if form.is_valid():
            # 유효하면 저장
            article = form.save()
            return redirect('articles:detail', article.pk)
        # 유효하지 않다면 !
        return redirect('articles:index')
    
        # # 사용자의 입력 데이터를 받아서
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        
        # # 게시글을 생성한다 -> DB에 저장
        # # 1. Article 인스턴스를 만들어서 저장.
        # article = Article()
        # article.title = title
        # article.content = content
        # article.save()
        
        # # 2. 
        # article = Article(title = title, content=content)
        # article.save()
        
        # # 3. objects 매니저의 create 
        # Article.objects.create(title=title, content=content)
        
        # # 모든 게시글에 대한 페이지로 화면 이동해라
        # return redirect('articles:index')
        # 디테일 페이지로 화면을 이동해라
        # return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/create.html', context)

# 특정 게시글을 삭제
def delete(request, pk):
    # pk에 해당하는 게시글을 삭제하겟다
    article = Article.objects.get(pk=pk)
    article.delete()
    
    # 전체 게시글 페이지로 돌아가기
    return redirect('articles:index')

# def edit(request, pk):
#     article =Article.objects.get(pk=pk)
#     context = {
#         'article':article
#     }
#     return render(request, 'articles/edit.html', context)

def update(request, pk):
    if request.method =="POST":
        # 사용자가 전달한 데이터를 가져온다.
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 게시글 수정
        # 해당 게시글 정보를 DB로부터 가져오기
        article = Article.objects.get(pk=pk)
        
        # 제목과 내용 수정
        article.title = title
        article.content = content
        
        # 저징
        article.save()
        
        # 사용자게에 페이지 정보를 전달
        return redirect('articles:detail', article.pk)
    else:
        article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/update.html', context)
