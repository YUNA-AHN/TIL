from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('articles/', views.index, name = 'index'), #articles: index
]