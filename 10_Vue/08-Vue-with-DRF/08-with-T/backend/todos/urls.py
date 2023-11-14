from . import views
from django.urls import path

app_name="todos"
urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("/<int:pk>", views.todo_detail,name='todo_detail')
]
