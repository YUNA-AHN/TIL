from django.urls import path
from . import views


urlpatterns = [
    path('musics/', views.music_list),
    path('musics/<int:music_pk>/', views.music_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('musics/<int:music_pk>/comments/', views.comment_create),
]
