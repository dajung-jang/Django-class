from django.urls import path

# 현재디렉토리로 부터 views.py
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('signup/', views.signup, name = 'signup'),
]