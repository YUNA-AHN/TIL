from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from .models import Todo
from .serialrizers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# Todo 모델에 대한 CRUD

# 게시글 전체 조회 : CR
@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        # todos = get_list_or_404(Todo)
        serializer =TodoSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
            


# 게시글 상세 조회 : RUD
@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    