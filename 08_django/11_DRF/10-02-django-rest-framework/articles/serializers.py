from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    # override
    class ArticletitleSerializer(serializers.ModelSerializer):
        class Meta:
            model= Article
            fields = ('title',)
    article = ArticletitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


# fields: 결과물 출력, vaildataion 대상
# fields = '__all__' 이면 모든 필드가 늘 검증 대상
class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only = True)

    class Meta:
        model = Article
        fields = '__all__'

