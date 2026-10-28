from django.contrib import admin

# django.contrib.auth : django가 기본적으로 제공하는 패키지
from django.contrib.auth.admin import UserAdmin

from .models import User

# admin 사이트에 등록하겠다. User모델을 UserAdmin에 
admin.site.register(User, UserAdmin)