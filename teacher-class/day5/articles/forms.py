from django import forms
from .models import Articles

# form 태그와 Modelform 차이
# 사용자로부터 입력받은 데이터를 DB에 바로 저장 가능 한지 안한지
# form 태그도 DB에 저장 가능하지만, 소스코드 로직을 구현해야함
# 결론 : 효율성 좋고 + 유효성 검사에 용이해서 ModelForm 쓰는 거임

class ArticleForm(forms.ModelForm):
    # 모델폼의 기본구조를 자ㄷㅎㅇ으로 생성 --> 위젯이나 필드 선택을 통해서 세부 조정은 가능
    class Meta:
        model = Articles
        fields = '__all__'
        # 위의 코드랑 같은 의미 / 맨 뒤애 후행쉼표 꼭 붙여야 함
        # fields = ('title', 'content', 'created_at', 'updated_at', )