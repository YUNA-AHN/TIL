from django.urls import path
from . import views

app_name = 'weathers'
urlpatterns = [
    path('', views.index),
    path('problem1/', views.problem1, name = 'problem1'),
    path('problem2/', views.problem2, name ='problem2'),
    path('problem3/', views.problem3, name ='problem3'),
    path('problem4/', views.problem4, name ='problem4'),
]
