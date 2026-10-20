from django.shortcuts import render, redirect
from .forms import ArticleForm

# Article 로 만들어야헸는데 테이블을 Articles 로 잘못 만들었음
# 현재 디렉토리에서 models.py 들어가서 Articles 모델(DB 테이블) 가져오겠다.
from .models import Articles

def index(request):
    # QuerySet API --> 전체 데이터 조회
    # Articles.objects.all()
    articles = Articles.objects.all()

    context = {
        'articles': articles
    }
    # articles 폴더의 index.html 파일을 렌더링하겠다. 그리고 context 값도 같이 넘겨줌
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # QuerySet API --> 단일 게시글 조회 : get
    # get() 안에서 뒤의 pk == detail 함수 매개변수 pk == urls.py 의 detail path에 적힌 pk == index.html 의 a태그의 url 태그에 article. 뒤에 적힌 pk
    article = Articles.objects.get(pk = pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

"""
# html 의 form 태그 사용 할 때 코드

# 게시글 새로 작성하기 위한 페이지 로드
def new(request):
    return render(request, 'articles/new.html')

# 게시글 생성하는 함수(db로 정보 넘겨주기)
def create(request):
    # ORM 에서 create 의 3가지 방법
    # POST : POST 방식, .get : 딕셔너리 메서드(키 조회하는 메서드)
    # get() 괄호 안에 넣은 키 값 == new.html 에서 form 태그 안에 각 태그에 있는 name 속성에 적힌 값
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 저장은 2번 방법 (유효성 검사 때문에 이 방법 씀)
    # 시간대는 자동완성이어서 title, content 만 넣어주면 됨
    article = Articles(title = title, content = content)

    # 데이터 관리 원칙 : 안전성, 보안성
    # save 하기 전에 반드시 유효성 검사를 해야한다!!!
    article.save()

    return redirect('articles:detail', article.pk)
"""

""" ModelForm 사용 방식 """
def create(request):
    # 1. 내가 게시글 생성 버튼 눌렀을 때 (POST 요청)
    if request.method == "POST" :
        # print(reqeust.POST) 하면 ==> title, content 나옴 (사용자가 입력한 거)
        # request.FILES -> 업로드한 데이터
        form = ArticleForm(request.POST, request.FILES)    
        # 유효성 검사
        if form.is_valid():     # 주관식 단골 문제
            article = form.save()
            # POST 요청 + DB 에 저장 ==> 리다이랙트
            return redirect('articles:detail', article.pk)
    
    # 2. 내가 글쓰기 버튼 눌렀을 때 (html 페이지 들어갔을 때)
    # == POST 요청이 아닐 때 ==> 게시글 생성 버튼 누르기 전 or 유효성 검사 실패했을 때
    else:
        form = ArticleForm()
        # GET 요청인 경우
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

'''
# modelForm 사용 안 할 때 쓰는 거
# CREATE 와 차이 : UPDATE 는 전에 있던 게시글을 조회 해야함
def edit(request, pk):
    article = Articles.objects.get(pk = pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

# 리다이랙트 : (CRATE 와 차이 : 기존에 있던 게시글을 변경)
def update(request, pk):
    article = Articles.objects.get(pk = pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)
'''

# modelForm 사용 시
def update(request, pk):
    # 우선 기존에 있던 게시글을 조회 (QuerySetAPI)
    article = Articles.objects.get(pk = pk)

    # 1. POST 요청일 때
    if request.method == 'POST':
        # instance = article (기존에 있던 데이터를 미리 채우기)
        form = ArticleForm(request.POST, request.FILES, instance = article)
        # 유효성 검사
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    # 2. POST요청이 아닐 때
    else:
        form = ArticleForm(instance= article)

    # GET요청
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

# POST 요청 -> 리다이랙트
def delete(request, pk):
    # "조회" 후 삭제
    article = Articles.objects.get(pk = pk)
    article.delete()
    
    return redirect('articles:index')