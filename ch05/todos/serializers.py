from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer[Todo]):
    class Meta:
        model = Todo
        fields = (
            "id",
            "title",
            "body",
        )
