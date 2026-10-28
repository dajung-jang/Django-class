from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# User 모델을 가져와야 한다. (models.py 로부터 가져왔다)
# from .models improt User -> 직접 참조

# get_user_model -> 간접 참조
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # model = User -> 직접 참조
        model = get_user_model()    # 간접 참조
        
