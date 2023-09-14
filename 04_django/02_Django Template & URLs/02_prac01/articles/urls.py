from django.urls import path
from . import views

# articles
app_name = 'articles'
urlpatterns = [
    # path('', views.dummy),
    path('home/', views.index, name = 'home'),
    path('greeting/', views.greeting, name = 'greeting'),
    path('greeting2/', views.greeting2, name = 'greeting2'),
]
