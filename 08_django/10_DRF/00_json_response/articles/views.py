from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .serializers import ArticleSerializer
from .models import Article

# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    # JsonResponse 클래스 객체를 통해서 응답 JSON 형태
    # 기본적인 파이썬 자료형 데이터를 만들어야 할 필요가 있다! (딕셔너리, 리스트)
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

from django.core import serializers
def article_json_2(request):
    articles = Article.objects.all()
    # json으로 변경 예정
    data = serializers.serialize('json', articles)

    # data = '{"name":"홍길동" ,"score" : 100,"age" : 17}'
    # 문자열 통째로 반환, json 형태로
    return HttpResponse(data, content_type='application/json')


# @api_view(['GET'])
@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
