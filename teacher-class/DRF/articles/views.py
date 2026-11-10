from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
# list : 전체 객체 조회 -> 객체가 하나도 없다 : 404 예외 발생 시킴
# object : 단일 객체 조회 -> 객체가 없다 : 404 예외 발생 시킴
# 4xx 에러 : 클라이언트 에러
# 5xx 에러 : 서버 에러
# 404 에러 : Not Found
from django.shortcuts import get_object_or_404, get_list_or_404

# GET : 전체 게시글 조회, POST : 게시글 생성
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        # 객체가 여러개(다중 데이터) 일때 : many = True 
        serializer = ArticleListSerializer(articles, many=True)
        # 직렬화 된 데이터를 json 형태로 응답
        return Response(serializer.data)
    elif request.method == 'POST':
        # 사용자가 입력한 데이터 -> request.data
        serializer = ArticleSerializer(data = request.data)
        #  유효성 검사
        # raise_exception=True -> 유효하지 않을 경우 예외 발생
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 데이터 생성을 성공/실패 -> 성공하면 201, 실패하면 400
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # 단일 게시글 조회
    article = get_object_or_404(Article, pk=article_pk)
    # 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    # 삭제
    elif request.method == 'DELETE':
        article.delete()
        # 204: 성공, 반환할 콘텐츠가 없음
        return Response(status=status.HTTP_204_NO_CONTENT)
    # 수정
    elif request.method == 'PUT':   
        # partial=True: 부분 업데이트를 허용 (일부 필드만 수정이 가능하다)
        serializer = ArticleSerializer(
            article, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
        

    