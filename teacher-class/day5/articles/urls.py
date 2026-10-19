from django.urls import path
# 현제 디렉토리로부터 views.py
from . import views

app_name = "articles"

urlpatterns = [
    # 전체 게시글 조회
    # https://127.0.0.1:8000/articles/ 로 url 요청 오면 
    # views.py 의 index 함수를 실행하겠다
    path("index/", views.index, name = "index"),
    # <int:pk> => variable routing
    path('<int:pk>/', views.detail, name = 'detail'),
    # CREATE : 렌더링 + 리다이랙트
    # 게시글 생성 페이지를 띄운다 -> get 요청(랜더링)
    # 게시글 작성하고 그 게시글을 생성한다 -> DB 가 바뀜 -> post 요청 (리다이랙트)
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
    # UPDATE(전에 있던 데이터 불러와야함) : 렌더링 + 리다이렉트
    path('<int:pk>/edit/', views.edit, name= 'edit'),
    path('<int:pk>/update', views.update, name = 'update'),
    # DELETE -> 게시글 조회 후 삭제
    path('<int:pk>/delete', views.delete, name = 'delete'),
]