from django.contrib import admin

# 현재 디렉토리의 models.py로 부터 Article 모델을 가죠온다
from .models import Article

# Article 모델을 admin 사이트에 등록하겟다
admin.site.register(Article)
