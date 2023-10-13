from django.urls import path
from . import views

app_name = 'trends'
urlpatterns = [
    path('keyword/', views.keyword, name = 'keyword'),
    path('keyword/<int:pk>/', views.keyword_delete, name = 'keyword_delete'),
    path('crawling/', views.crawling, name = 'crawling'),
    path('crawling/histogram/', views.crawling_histogram, name = 'crawling_histogram'),
    path('crawling/advanced/', views.crawling_advanced, name = 'crawling_advanced'),
    
]
