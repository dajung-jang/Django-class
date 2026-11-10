from rest_framework import serializers

from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # 내가 직렬화 하고자 하는 필드들
        fields = (
            'id',
            'title',
            'content',
        )

class ArticleSerializer(serializers.ModelSerializer):
    # 반드시 단일 댓글이 단독으로 생성되거나 할 수 없음
    # 특정 게시글(1)에 작성되어있는 댓글(N)
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = (
                'id',
                'content',
            )
    # 필드를 2개 추가 (읽기전용 필드)
    # 1. 사용자로부터 입력받거나 수정할 수 없다
    # 2. 유효성 검사로부터 제외
    # 3. 입력받지 않고, 유효성검사에서 제외되지만 클라이언트에 제공
    comment_set = CommentDetailSerializer(many=True, read_only=True)
    # 중욧!!!
    # comment_set : 역참조, count : 메서드
    comment_count = serializers.IntegerField(
        source = 'comment_set.count', read_only=True
    )

    class Meta:
        model = Article
        # '__all__' : 모든 필드
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    # 댓글 조회할 때 게시글의 제목도 같이 조회가 되게
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title', )
    
    # 중요!!! 댓글 조회 했을때 같이 볼 수 있는 게시글의 제목은 "읽기 전용"
    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
    
