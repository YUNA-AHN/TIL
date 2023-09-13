from django.shortcuts import render
import random
from django.http import HttpResponse

# Create your views here.
def dinner(request):
    foods = ['A코너', 'C코너', '테이크아웃']
    pick = random.choice(foods)
    context = {
        'foods' : foods,
        'pick' : pick,
    }
    return render(request, 'pages/dinner.html', context)

def dummy(request):
    return HttpResponse('<h1>여기로 빠졌수다.</h1>')

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'pages/catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'pages/hello.html', context)