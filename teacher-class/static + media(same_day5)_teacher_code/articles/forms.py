from django import forms
from .models import Article

# form태그와 ModelForm의 차이
# 사용자로부터 입력받은 데이터를 DB에 바로 저장가능 하는지 안하는지
# form태그도 DB에 저장 가능하지만, 소스코드 로직을 구현해야함
# 결론 : 효율성좋고 + 유효성 검사에 용이해서 ModelForm을 쓰는거다

class ArticleForm(forms.ModelForm):
    # 모델폼의 기본구조를 자동으로 생성 ---> 위젯이나 필드선택을 통해서 세부 조정은 가능
    class Meta:
        model = Article
        # fields = ('title', 'content', 'created_at', 'updated_ad', )
        fields = '__all__'