from django.shortcuts import render

def index(request):
    # context 딕셔너리 구조
    # templates(.html)에서 context에 key로 접근하면 value 값 가져올 수 있음
    context = {
        'name': 'Jane',
        'number': 1
    }
    # context 가 있을 경우 반드시 3번째 인자로 context
    return render(request, 'articles/index.html', context)

import random

def dinner(request):
    foods = ['삼겹살', '족발', '치킨', '이재모 피자']

    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked
    }

    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # throw 가 던진걸 받아야함
    # GET 방식으로 던진걸 받을거다
    # GET: GET 방식, get: 딕셔너리 메서드
    text = request.GET.get('throw')

    context = {
        'text': text
    }
    return render(request, 'articles/catch.html', context)