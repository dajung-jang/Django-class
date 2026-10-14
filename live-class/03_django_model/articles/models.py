from django.db import models

# Create your models here.

# 게시글 저장을 위한 테이블 설계
# 우리가 DB와 상호작용하는 것을 직접 개발하려면 굉장히 많은 것들을 고려해야 함
# 보안, 어떤 방식으로 소통을 할지, 여러 기능들(수정, 삭제 등등 ..)
# 그래서 Django는 이러한 기본적인 설계 기능을 미리 구현해 놨음 ==> models 모듈에 구현 해놓음
# 우리가 해야하는 건 그냥 models 모듈에서 필요한 클래스, 함수들을 잘 가져다가 사용 하는 것
# 기본적인 model class 에 대한 구현이 완료된 Model 클래스를 상속 받으면서 시작
class Article(models.Model):
    # 우리는 Model 클래스를 상속 받으면서 다른 것들을 고민할 필요 없이
    # 지금 해야할 것(테이블의 칼럼을 정의하고, 여러 제약조건들을 정의하는 일)에 대해서만 개발할 수 있음
    # 컬럼을 정의할 때 id 컬럼은 Django 가 알아서 만들어 줌
    # 컬럼은 클래스 변수로 정의
    # 컬럼의 기본 틀(클래스) 자체도 django 가 제공 해줌
    title = models.CharField(max_length=10, null=False, blank=False)  # 클래스를 통해 인스턴스를 만들어주는 것 / null, blanke를 작성하지 않으면 지금 작성된 것처럼 false로 default 값이 작성 되어 있는것 -> 만약 다른 값으로 작성하려면 작성해주면 됨
    content = models.TextField()
    # 추가 필드 정의 (위의 필드 정의하고 db에 정의까지 다 하고 난 다음) -> 이러면 터미널에서 py manage.py makemigation 쳤을 때오류남 (추가 필드에 default 값이 정의 되어 있어야 추가할 수 있음) -> 직접 default 값 작성해주거나, 장고가 해주는거 선택할 수 있음-> 터미널에서 1번 누르면 default 값 작성해달라고 함 -> 그냥 바로 enter 누르면 default로 설정되어 있는 값을 default 값 넣어줌
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)