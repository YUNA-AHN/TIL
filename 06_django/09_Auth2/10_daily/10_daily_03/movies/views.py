from django.shortcuts import redirect, render, get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required
# Create your views here.

@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request,'movies/index.html',context)

@login_required
@require_http_methods(["GET","POST"])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid:
            movie = form.save()
            return redirect('movies:detail',movie.pk)
    else:
        form = MovieForm()
    context={
        'form':form
    }
    return render(request,'movies/create.html',context)

@require_safe
def detail(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    context = {
        'movie':movie,
    }
    return render(request,'movies/detail.html',context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie,pk=pk)
        movie.delete()
    return redirect("movies:index")


@login_required
@require_http_methods(["GET","POST"])
def update(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance = movie)
        if form.is_valid:
            form.save()
            return redirect("movies:detail",movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie':movie,
        'form':form,
    }
    return render(request,"movies/update.html",context)

