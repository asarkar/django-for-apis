from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer[Post]):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "title",
            "body",
            "created_at",
        )
        model = Post
