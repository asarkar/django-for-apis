from books.models import Book
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class BookTests(APITestCase):
    book: Book

    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title="A good title",
            subtitle="An excellent subtitle",
            author="Tom Christie",
            isbn="1234567890123",
        )

    def test_api_listview(self) -> None:
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book.title)
