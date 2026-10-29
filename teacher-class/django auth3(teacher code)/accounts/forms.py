from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# User 모델을 가져와야한다 (models.py로부터 가져왔다)
# from .models import User -> 직접참조

# get_user_model -> 간접참조

from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # model = User -> 직접 참조
        model = get_user_model() # 간접 참조        

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # 회원정보 변경할때 작성할 필드
        fields = ('first_name', 'last_name', 'email',)