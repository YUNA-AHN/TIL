from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)


class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    # 첫 번째 방법
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # 역참조 이름 변경한 이후
    # comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # 두 번째 방법
    # comment_set = CommentListSerializer(many=True, read_only=True)
    # 역참조 이름 변경한 이후
    comments = CommentListSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'