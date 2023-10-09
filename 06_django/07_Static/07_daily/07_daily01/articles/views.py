from django.shortcuts import redirect, render, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_POST, require_http_methods, require_safe

# Create your views here.

@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request,'articles/index.html',context)

@require_http_methods(["GET","POST"])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm()
    context={
        'form':form
    }
    return render(request,'articles/create.html',context)

@require_safe
def detail(request,pk):
    article = get_object_or_404(Article,pk=pk)
    context = {
        'article':article,
    }
    return render(request,'articles/detail.html',context)

@require_POST
def delete(request,pk):
    article = get_object_or_404(Article,pk=pk)
    article.delete()
    return redirect("articles:index")

@require_http_methods(["GET","POST"])
def update(request,pk):
    article = get_object_or_404(Article,pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance = article)
        if form.is_valid():
            form.save()
            return redirect("articles:detail",article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article':article,
        'form':form,
    }
    return render(request,"articles/update.html",context)

