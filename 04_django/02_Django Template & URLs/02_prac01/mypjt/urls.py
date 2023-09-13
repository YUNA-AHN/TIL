"""
URL configuration for mypjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from articles import views as articles_views
from pages import views as pages_views

urlpatterns = [
    # articles에 있는 urls.py에 맵핑을 위임
    path('articles/', include('articles.urls')),
    # articles에 있는 pages.py에 맵핑을 위임
    path('pages/', include('pages.urls')),
    
    # # 세세한 경로를 위에서 먼저 지정
    # # path('', views.dummy),
    # # articles
    # path('admin/', admin.site.urls),
    # path('home/', articles_views.index),
    # path('greeting/', articles_views.greeting),
    # path('greeting2/', articles_views.greeting2),
    # # pages
    # path('dinner/', pages_views.dinner),
    # path('throw/', pages_views.throw),
    # path('catch/', pages_views.catch),
    # path('hello/<name>/', pages_views.hello),
]
