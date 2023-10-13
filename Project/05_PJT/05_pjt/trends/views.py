from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .forms import KeywordForm

from bs4 import BeautifulSoup
from selenium import webdriver

import matplotlib.pyplot as plt
# 그래프 그리기 위한 사전 준비
from io import  BytesIO
import base64
plt.switch_backend('Agg')
plt.rcParams['font.family'] = 'Malgun Gothic'



# Create your views here.
def keyword(request):
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trends:keyword')
    else:
        form = KeywordForm()

    keywords = Keyword.objects.all()
    context = {
        'keywords' : keywords,
        'form' : form
    }
    return render(request, 'trends/keyword.html', context)

def keyword_delete(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')

def crawling(request):
    # pass
    
    keywords = Keyword.objects.values('name')
    
    def get_google_data(keyword):
        url = f'https://www.google.com/search?q={keyword}'

        # 크롬 브라우저가 열림
        # 이 때, 동적인 내용들이 모두 채워진다.
        driver = webdriver.Chrome()
        driver.get(url)

        # 열린 페이지 소스를 받아옴
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 검색 결과 가져오기
        # div  태그 안의 id가 result-stats 라는 요소
        result_stats = soup.select_one('div#result-stats')
        nums = result_stats.text.split()[2][:-1]
        result_search = int(''.join(nums.split(',')))
        
        return keyword, result_search


    for kw in keywords:
        name, result = get_google_data(kw['name'])
        # name이 있으면.. update... 없으면 save...
        if Trend.objects.filter(name=name).exists():
            # 존재하면 
            trends = Trend.objects.get(name=name)
            trends.result = result
            
        else: # 존재하지 않는다면
            trends = Trend(name=name, result=result, search_period = 'all')
        trends.save()

    keywords = Keyword.objects.all()
    trends = Trend.objects.all()
    context = {
        'trends' : trends,
    }
    return render(request, 'trends/crawling.html', context)

def crawling_histogram(request):
    data = Trend.objects.values_list('name', 'result')
    name_lst = []
    result_lst = []
    for name, result in data:
        name_lst.append(name)
        result_lst.append(result)

    plt.clf()
    plt.bar(name_lst, result_lst)
    plt.grid()
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.legend( name_lst, loc = 'upper right')
    
    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    image_base64 =  base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    
    context  = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'trends/crawling_histogram.html', context)


def crawling_advanced(request):
    keywords = Keyword.objects.values('name')
    
    def get_google_data(keyword):
        url = f'https://www.google.com/search?q={keyword}&source=lnt&tbs=qdr:y'

        # 크롬 브라우저가 열림
        # 이 때, 동적인 내용들이 모두 채워진다.
        driver = webdriver.Chrome()
        driver.get(url)

        # 열린 페이지 소스를 받아옴
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 검색 결과 가져오기
        # div  태그 안의 id가 result-stats 라는 요소
        result_stats = soup.select_one('div#result-stats')
        nums = result_stats.text.split()[2][:-1]
        result_search = int(''.join(nums.split(',')))
        
        return keyword, result_search


    for kw in keywords:
        name, result = get_google_data(kw['name'])
        # name이 있으면.. update... 없으면 save...
        if Trend.objects.filter(name=name).exists():
            if not Trend.objects.filter(name=name, search_period='year').exists():
                trends = Trend(name=name, result=result, search_period = 'year')
                trends.save()
        else: # 존재하지 않는다면
            trends = Trend(name=name, result=result, search_period = 'year')
            trends.save()

    # 그래프
    data = Trend.objects.filter(search_period='year').values_list('name', 'result')
    name_lst = []
    result_lst = []
    for name, result in data:
        name_lst.append(name)
        result_lst.append(result)

    plt.clf()
    plt.bar(name_lst, result_lst)
    plt.grid()
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.legend( name_lst, loc = 'upper right')
    
    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    image_base64 =  base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    
    context  = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    
    return render(request, 'trends/crawling_advanced.html', context)