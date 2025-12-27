from books.models import Book
from rest_framework import generics

from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView[Book]):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
