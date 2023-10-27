from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings
from django.db.models import Max

from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, DepositProductsListSerializer


# Create your views here.
BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'
API_KEY = settings.API_KEY

@api_view(['GET'])
def index(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth' : settings.API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }
    response = requests.get(URL, params=params).json()['result']
    return Response({'response' : response})

@api_view(['GET'])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth' : settings.API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }
    response = requests.get(URL, params=params).json()['result']

    # baseList
    for item in response.get('baseList'):
        save_data = {
            'fin_prdt_cd': item.get('fin_prdt_cd'),
            'kor_co_nm': item.get('kor_co_nm'),
            'fin_prdt_nm': item.get('fin_prdt_nm'),
            'etc_note': item.get('etc_note'),
            'join_deny': item.get('join_deny'),
            'join_member': item.get('join_member'),
            'join_way': item.get('join_way'),
            'spcl_cnd': item.get('spcl_cnd'),
        }
        serializer = DepositProductsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # optionList
    for item in response.get('optionList'):
        save_data = {
            'fin_prdt_cd': item.get('fin_prdt_cd'),
            'intr_rate_type_nm': item.get('intr_rate_type_nm'),
            'intr_rate': item.get('intr_rate'),
            'intr_rate2': item.get('intr_rate2'),
            'save_trm': item.get('save_trm'),
        }
        for elem in save_data:
            if not save_data[elem]:
                save_data[elem] = -1

        serializer = DepositOptionsSerializer(data = save_data)
        product =  DepositProducts.objects.get(fin_prdt_cd = save_data['fin_prdt_cd'])
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)

    return Response({'response' : response})

@api_view(['GET','POST'])
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsListSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message':'이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다.'})

# 특정 상품의 옵션 리스트 출력
# 해당 상품의 옵션 리스트를 출력
# B번에서 확인한 상품 리스트의 가장 첫번째 상품 fin_prdt_cd 활용
@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)

# 금리가 가장 높은 상품의 정보 출력
# 금리가 가장 높은 상품의 상세정보와 옵션을 반환
# 저축기관에 상관없이 최고 우대 금리 기준 desc
@api_view(['GET'])
def top_rate(requset):
    # 우대 금리 높은 순으로 정렬
    max_rate = DepositOptions.objects.aggregate(Max('intr_rate2'))['intr_rate2__max']
    # 가장 높은 옵션 뽑기
    option = DepositOptions.objects.get(intr_rate2=max_rate)
    options = DepositOptions.objects.filter(intr_rate2=max_rate)
    print(option)
    
    # 가장 높은 옵션을 가진 상품 출력
    product = DepositProducts.objects.get(fin_prdt_cd=option.fin_prdt_cd)

    # 상품
    serializer1 = DepositProductsListSerializer(product)
    serializer2 = DepositOptionsSerializer(options, many=True)

    save_data = {
        'deposit_product':serializer1.data,
        'options':serializer2.data,
    }

    return Response(save_data)