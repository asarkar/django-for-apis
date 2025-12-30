from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer[Post]):
    author = serializers.SlugRelatedField(
        queryset=get_user_model().objects.all(), slug_field="username"
    )

    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at",
        )
        model = Post


class UserSerializer(serializers.ModelSerializer):  # type: ignore[type-arg] # Don't hardcode user model
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
        )
