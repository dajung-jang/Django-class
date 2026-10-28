from django.shortcuts import render, redirect

# article할때는 ModelForm
# auth할때는 built-in form 
from django.contrib.auth.forms import (
    AuthenticationForm, # 로그인을 위한 폼
    UserCreationForm, # 계정 생성 위한 폼 (회원가입)
    PasswordChangeForm # 비밀번호 변경을 위한 폼
)

# 로그인, 로그아웃 기능
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User


# 로그인 페이지를 띄우고 아이디 페스워드 입력하고 로그인버튼 누른다
def login(request):
    # 로그인버튼 누른다
    if request.method == 'POST':
        # AuthenticationForm : built-in form
        # request.POST : 아이디, 패스워드 (사용자가 입력한)
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # get_user() : 인증된 사용자의 객체
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else: # GET요청 X (POST요청이 아닐때)  
        form = AuthenticationForm() # 빈 폼
    # GET 요청 or 유효성 검사 실패했을때
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    # 로그아웃 페이지가 따로 있나요?? X
    return redirect('articles:index')