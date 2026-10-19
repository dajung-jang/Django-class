from django.contrib import admin

# Register your models here.
# 현재 디렉토리의 models.pu 의 Article 모델을 가져오기ㅖㅆ다
from . models import Articles

# admin 사이트에 등록하겠다
admin.site.register(Articles)
