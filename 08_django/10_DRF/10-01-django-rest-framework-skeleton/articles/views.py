from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

from rest_framework import status

@api_view(['GET','POST'])
def article_list(request):
    # Read 전체 게시물 조회
    # - "articles/" GET
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many = True)
        return Response(serializer.data)
    # Create 게시물 생성
    # - "articles/" POST
    elif  request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        # raise_exception를 설정해주면 유효성 검사 통과 못하는 경우
        # 자동으로 404로 넘어감
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


    
@api_view(['GET','DELETE', 'PUT'])
def article_detail(request, article_pk):
    # Read 특정 게시물 조회
    # - "articles/<int:article_pk>/" GET
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer =  ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)