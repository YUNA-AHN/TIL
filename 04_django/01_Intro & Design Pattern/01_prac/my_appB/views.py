from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello2(request):
    return render(request, 'my_appB/hello2.html')

def greet(request):
    return render(request, 'my_appB/greet.html')