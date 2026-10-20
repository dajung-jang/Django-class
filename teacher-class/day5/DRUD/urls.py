from django.contrib import admin
# include -> url 매핑
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # articles 앱의 urls.py 로 
    # (articles 앱(include 괄호 안에 적혀있는 앱)의 urls 에 적힌 경로는 url 경로를 'articles/' 뒤에 다 붙이겠다는 의미)
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
