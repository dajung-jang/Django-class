from django.shortcuts import render

def index(request):
    # render(): 풀스택 개발에서만 사용 / 페이지 렌더링(index.html 을 렌더링)
    return render(request, 'articles/index.html')
