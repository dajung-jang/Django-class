from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


# 로그인 : 세션을 CREATE 하는 로직이다.
def login(request):
    # 1. POST 요청일 때 새션을 생성 (+인증)
    if request.method == 'POST':
        # POST에 담겨진 사용자 입력 데이터를 받음 (modelform 은 첫번째 인자가 data여서 그냥 request.POST 쓰면 됐지만, form 은 첫번째 인자가 request여서 앞에 request를 붙여줌 (create함수 안에서 articleForm은 modelform))
        # AuthenticationForm의 부모 클래스인 Form 의 생성자 함수 인자 구성의 첫번째 인자는 request다
        form = AuthenticationForm(request, request.POST)
        # 유효성 검사
        if form.is_valid():
            # 세션 데이터를 생성 (login 빌트인 함수가 진행 -> 빌트인 함수니까 import 필요)
            # 인자 두개 받음 = auth_login(요청 객체, 인증된 유저 객체)
            # AuthenticationForm이 제공하는 인스턴스 메서드 get_user 메서드가 인증된 유저 객체를 반환 해줌
            user = form.get_user()
            auth_login(request, user)
            return redirect('articles:index')


    # 2. POST 요청이 아닐 때는 로그인 페이지를 응답
    else:
        # AuthenticationForm = 얘는 modelform 이 아니라 그냥 form임
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
