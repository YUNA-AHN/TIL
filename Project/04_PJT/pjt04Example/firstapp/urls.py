from django.urls import path
from . import views

# 앱이 하나니까 굳이 app_name 설정해주지 않아도 된다..!
urlpatterns = [
    path('', views.index),
    path('example/', views.example),
]