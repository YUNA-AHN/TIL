from django.urls import path
from . import views

app_name = 'libraries'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/review/', views.review_create, name='review_create'),
    path('<int:book_pk>/review/<int:review_pk>/delete/',
          views.review_delete, name='review_delete'),
]
