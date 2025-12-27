from books.models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer[Book]):
    class Meta:
        model = Book
        fields = ("title", "subtitle", "author", "isbn")
