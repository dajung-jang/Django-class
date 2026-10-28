from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# # 우리가 대체한 User 클래스
# from .models import User

# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         # 우리가 대체한 User 클래스로 교체
#         model = User

# Django는 User 객체를 직접 참조해서 활용하는 것을 권장하지 않음
# 대신에 현재 Django에서 활성화된 User 모델 클래스를 자동으로 반환해주는 함수를 제공 => get_user_model()
from django.contrib.auth import get_user_model

# 회원가입 할 때(signup 함수) 사용
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 우리가 대체한 User 클래스로 교체
        model = get_user_model()

# 회원 정보 수정할 때(update 함수) 사용
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        # 우리가 대체한 User 클래스로 교체
        model = get_user_model()
        # form 에서 보여즐 정보 선택 (기본은 all 로 되어있어서 일반 사용자들이 보면 안되는 정보들이 보여짐-> 관리자로 선택할건지 권환은 뭘 가질건지 등등 => 일반 사용자가 수정하면 안되는 정보들)
        fields = ('first_name', 'last_name', 'email',)
        