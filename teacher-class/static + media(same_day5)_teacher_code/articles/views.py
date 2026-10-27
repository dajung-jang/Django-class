from django.shortcuts import render, redirect

# Create your views here.

# 현재 티렉토리에서 models.py로부터 Aritlce모델 가져오겠다.
from .models import Article

def index(request):
    # QuerySet API ---> 전체 데이터 조회
    # Article.objects.all()
    articles = Article.objects.all()

    context = {
        'articles': articles
    }
    # articles폴더의 index.html 파일을 랜더링하겠다
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # QuerySet API ---> 단일 게시글 조회 : get
    article = Article.objects.get(pk = pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

from django.shortcuts import render, redirect
from .forms import ArticleForm


def create(request):
    # 1. 내가 게시글 생성 버튼 눌렀을때 (POST 요청)
    if request.method == 'POST':
        # print(request.POST) -> title, content
        # request.FILES -> 업로드한 데이터
        form = ArticleForm(request.POST, request.FILES)
        # 유효성 검사
        if form.is_valid(): # 주관식 단골 문제 (스펠링 많이 틀림 주의!!)
            article = form.save()
            # POST요청 + DB에 저장
            return redirect('articles:detail', article.pk)


    # 2. POST요청이 아닐때 -> 게시글 생성 버튼 누르기전 or 유효성검사 실패했을 때
    else:
        form = ArticleForm()
        # GET 요청인 경우
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)






# 리다이렉트 : (CREATE와 차이 : 기존에 있던 게시글을 변경)
def update(request, pk):
    # 우선 기존에 있던 게시글을 조회 (QuerySetAPI)
    article = Article.objects.get(pk =pk)

    # 1. POST요청일때
    if request.method == 'POST':
        # instance = article (기존에있던 데이터를 미리 채우기)
        form = ArticleForm(request.POST, request.FILES, instance = article)
        # 유효성 검사
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)

    # 2. POST요청이 아닐때
    else:
        form = ArticleForm(instance = article)

    # GET 요청
    context = {
        'article': article,
        'form': form
    }
    return render(request, 'articles/update.html', context)

# POST요청 -> 리다이렉트
def delete(request, pk):
    # 조회후 삭제
    article = Article.objects.get(pk = pk)
    article.delete()
    return redirect('articles:index')