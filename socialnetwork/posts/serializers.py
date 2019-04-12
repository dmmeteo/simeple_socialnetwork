from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('url', 'id', 'author', 'sum_likes', 'sum_unlikes', 'text', 'release_date',)
        read_only_fields = ('url', 'id', 'author', 'sum_likes', 'sum_unlikes', 'release_date',)


class LikePostSerializer(serializers.Serializer):
    like = serializers.BooleanField(required=True)

    def update(self, validated_data):
        post = Post.objects.update(**validated_data)
        return post
