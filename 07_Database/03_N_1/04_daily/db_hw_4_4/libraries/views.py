from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Review
from .forms import ReviewFrom

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'libraries/index.html', context)

def detail(request, pk):
    book = Book.objects.get(pk=pk)
    review_form = ReviewFrom()
    reviews = book.review_set.all()
    context = {
        'book': book,
        'review_form' : review_form,
        'reviews' : reviews,
    }
    return render(request, 'libraries/detail.html', context)

@login_required
def review_create(request, pk):
    book = Book.objects.get(pk=pk)
    review_form = ReviewFrom(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.book = book
        review.user = request.user
        review_form.save()
        return redirect('libraries:detail', book.pk)
    context = {
        'book' : book,
        'review_form' : review_form,
    }
    return render(request, 'libraries/detail.html', context)

@login_required
def review_delete(request, book_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('libraries:detail', book_pk)