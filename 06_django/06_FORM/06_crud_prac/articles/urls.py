'''
# Article (게시글) CRUD
- 전역 경로 : articles/

뷰 함수 유형
1. 사용자에게 보여줘야할 html 파일을 랜더링  render
2. 사용자로부터 데이터를 받아서 처리

                                        경로 <-> 뷰 함수

'R'ead(조회)
- 전체 게시글 조회 :                                <-> index
- 상세 게시글 조회 :                    <int:pk>/   <-> deatil

'C'reate (생성)
- 게시글 생성에 필요한 폼을 사용자에게 제공 :   new/    <-> new
- 사용자로부터 정보를 받아 게시글 생성 :        create/  <-> create

'U'pdate(생성)
- 게시글 수정에 필요한 폼을 사용자에게 제공 :   <int:pk>/edit <-> eidt
- 사용자로부터 정보를 받아 게시글 수정 :        <int:pk>/update <-> update

'D'elete (삭제)
- 사용자로부터 삭제요청, 게시글을 삭제 :        <int:pk>/delete <-> delete
'''
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # 전체 게시글 조회
    path('', views.index, name='index'),
    # 상세 페이지 조회
    path('<int:pk>/', views.detail, name='detail'),
    # 게시글 생성에 필요한 폼을 사용자에게 제공
    # path('new/', views.new, name='new'),
    # 사용자로부터 
    path('create/', views.create, name='create'),
    # 게시물 삭제
    path('<int:pk>/delete/', views.delete, name='delete'),
    # 게시물 수정에 필요한 폼을 사용자에게 제공
    # path('<int:pk>/edit/', views.edit, name='edit'),
    # 정보를 받아 게시글 수정
    path('<int:pk>/update/', views.update, name='update'),
]