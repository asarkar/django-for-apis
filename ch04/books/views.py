from django.views.generic import ListView

from .models import Book


class BookListView(ListView):  # type: ignore[type-arg]
    model = Book
    template_name = "book_list.html"
