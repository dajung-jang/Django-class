from django.contrib import admin
from .models import Article

# admin site에 우리가 만든 Article 모델 클래스 등록
admin.site.register(Article)