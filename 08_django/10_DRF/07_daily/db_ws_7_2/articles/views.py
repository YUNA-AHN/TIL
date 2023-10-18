# many=True : Query set 또는 개체 목록을 직렬화할 때
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method =='GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method =='GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete' : f'데이터 {article_pk}번 글이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


    elif request.method =='PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)