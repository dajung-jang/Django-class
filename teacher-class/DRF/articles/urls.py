from django.urls import path
from articles import views

# app_name 안씀
# => templates 가 없기 때문에 안씀

urlpatterns = [
    # 전체 게시글 조회
    path('articles/', views.article_list),
    # 단일 게시글 조회, 게시글 삭제, 게시글 수정
    path('articles/<int:article_pk>/', views.article_detail),
    # 전체 댓글 조회
    path('comments/', views.comment_list),
    # 단일 댓글 조회, 삭제, 수정 (생성은 따로 빼는 이유: 생성할때 게시글 pk 를 베리어블 라우팅으로 가져와야해서 따로 뺌)
    path('comments/<int:comment_pk>/', views.comment_detail),
    # 댓글 생성은 단독으로 생성될 수 없음(오래키때무에)
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
