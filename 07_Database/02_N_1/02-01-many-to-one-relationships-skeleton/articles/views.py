from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'form' : form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article =  form.save(commit=False)
            article.author = request.user
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if article.user == request.user:
        article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid() and article.author == request.user:
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

def comment_create(request, pk):
    # pk인 게시글을 하나 조회하고
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # 그 게시글에 댓글을 작성한다 (유효성 검사를 위해 폼)
        form = CommentForm(request.POST)
        if form.is_valid():
            # 저장 save()를 하기전에
            # 먼저 comment 인스턴스에 article을 등록을 해줭야함
            # 이 과정을 먼저 수행해줘야함
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
        return redirect('articles:detail', pk)
    
def comment_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    comment.delete()
    redirect('articles:detail', pk)