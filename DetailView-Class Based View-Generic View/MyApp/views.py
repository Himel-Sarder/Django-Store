# myapp/views.py
from django.views.generic.detail import DetailView
from .models import Book

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
