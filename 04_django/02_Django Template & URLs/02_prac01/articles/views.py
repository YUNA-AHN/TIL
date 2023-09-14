from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def greeting(request):
    # context = {
    #     'name' : 'Alice'
    # }
    return render(request, 'articles/greeting.html', {'name' : 'Alice'})

def greeting2(request):
    foods = ['apple', 'banana', 'kiwi',]
    info = {
        'name' : '유나나씨'
    }
    context = {
        'foods' : foods,
        'info' : info,
    }
    return render(request, 'articles/greeting2.html', context)

def dummy(request, text):
    return HttpResponse(f'<h1>여기로 빠졌수다.{text}</h1>')