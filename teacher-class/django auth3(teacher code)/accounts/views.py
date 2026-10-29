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



from django.contrib.auth.decorators import login_required

# 로그인한 사용자만 로그아웃 할수있도록
@login_required
def logout(request):
    auth_logout(request)
    # 로그아웃 페이지가 따로 있나요?? X
    return redirect('articles:index')

from .forms import CustomUserCreationForm, CustomUserChangeForm

def signup(request):
    # is_authenticated : 인증된 사용자라면 (로그인이 되어있는데 회원가입 버튼을 눌렀다면)
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == "POST": # submit버튼 눌렀을때
        # request.POST -> 내가 회원가입할때 입력한 정보들
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): # 1. 유효성검사
            user = form.save() # 2. DB에 저장
            auth_login(request, user) # 3. 로그인
            return redirect('articles:index')
        
    else: # POST요청이 아닐때
        form = CustomUserCreationForm() # 빈폼

    # 유효성 검사 실패했다 or 처음 회원가입페이지 들어갈때
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

# 로그인된 사용자만 회원탈퇴 할수있음
@login_required
def delete(request):
    # 현재 로그인 되어있는 user
    request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == "POST":
        # request.POST : 사용자가 작성한 (first_name, last_name, email)
        # request.user : 로그인되어있는 user
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else: # POST요청이 아닐때 (submit 버튼 누르기 전)
        form = CustomUserChangeForm(instance = request.user)

    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)


from django.contrib.auth import update_session_auth_hash

@login_required
def password(request):
  if request.method == 'POST':
    # 첫 번째 인자는 user, 두 번째 인자는 데이터
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      # 세션 무효화 방지(자동 로그아웃 방지)
      # hash 함수로 현재 사용자의 인증 세션 갱신
      update_session_auth_hash(request, user)
      return redirect('articles:index')
  else:
    form = PasswordChangeForm(request.user)
  context = {
    'form' : form,
  }
  return render(request, 'accounts/password.html', context)

