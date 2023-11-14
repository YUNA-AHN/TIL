from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article

# Create your views here.
@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
