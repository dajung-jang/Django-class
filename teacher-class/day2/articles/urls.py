from django.urls import path
# 현재 폴더(디렉토리)로부터 views.py
from . import views

# 프로젝트가 1개 -> 앱이 여러개
# app_name 을 붙여줘야 앱이 여러개 더라도 다른 앱과 혼동이 안됨
# URL namespace
app_name = 'articles'

# name = "index" : named URL pattern
# html 에서 href = "https:// ~~~" 써서 url 작성 -> 그 대신 name으로 참조하겠다.
#  {% url 'articles:index' %} 

urlpatterns = [
    path('index/', views.index, name = "index"),
    path('dinner/', views.dinner, name = 'dinner'),
    path('search/', views.search, name = 'search'),
    path('throw/', views.throw, name = 'throw'),
    path('cathc/', views.catch, name = 'catch'),

]