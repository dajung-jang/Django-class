from django.urls import path

# 현재디렉토리로 부터 views.py
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('signup/', views.signup, name = 'signup'),
    path('delete/', views.delete, name = 'delete'),
    path('update/', views.update, name = 'update'),
    # 비밀번호 변경의 경우 url이 django 버전에 따라 다 다릅니다. 반드시 먼저 확인해야합니다.
    path('password/', views.password, name='password'),
]