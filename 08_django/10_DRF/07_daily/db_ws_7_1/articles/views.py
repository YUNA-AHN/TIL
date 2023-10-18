from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Article

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer

# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
    return JsonResponse(articles_json, safe=False)


def article_json_2(request):
    articles = Article.objects.all()
    # json으로 포맷 변환
    data = serializers.serialize('json', articles, fields=('title', 'content',))
    return HttpResponse(data, content_type='application/json')

# GET 요청만 허용할 수 있도록
@api_view(['GET'])
def article_json_3(request):
    articles = Article.objects.all()
    serializers =  ArticleSerializer(articles, many=True)
    return Response(serializers.data)