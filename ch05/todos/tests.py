from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo


class TodoModelTest(TestCase):
    todo: Todo

    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(title="First Todo", body="A body of text here")

    def test_model_content(self) -> None:
        self.assertEqual(self.todo.title, "First Todo")
        self.assertEqual(self.todo.body, "A body of text here")
        self.assertEqual(self.todo.title, "First Todo")

    def test_api_listview(self) -> None:
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo.title)

    def test_api_detailview(self) -> None:
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}), format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo.title)


class TodoAPITests(APITestCase):
    todo: Todo
    list_url: str
    detail_url: str

    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(title="Test Todo", body="Test body content")
        cls.list_url = reverse("todo_list")
        cls.detail_url = reverse("todo_detail", args=[cls.todo.id])

    def test_list_todo(self) -> None:
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 1)

    def test_detail_todo(self) -> None:
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.todo.title)
        self.assertEqual(response.data["body"], self.todo.body)

    def test_detail_todo_not_found(self) -> None:
        response = self.client.get(reverse("todo_detail", args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
