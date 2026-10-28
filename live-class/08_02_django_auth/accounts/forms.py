from django.contrib.auth.forms import UserCreationForm

'''
# 우리가 대체한 User 클래스
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 우리가 대채한 User 클래스로 교체
        model = User
'''

# 장고는 User 객체를 직접 참조해서 활용하는 것을 권장하지 않음
# 대신 장고에서 활정화된 User 모델 클래스를 자동으로 반환해주는 함수를 제공 -> get_user_model()
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 우리가 대채한 User 클래스로 교체
        model = get_user_model()