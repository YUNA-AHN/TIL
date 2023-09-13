from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('안녕하세용')

def menu(request):
    users = ['초밥', '파스타', '감자탕', '샌드위치']
    menus = ['강아지', '고양이', '곰돌이', '다람쥐']
    context = {
        'menus':menus,
        'users':users,
    }
    return render(request, 'my_app/index.html', context)
