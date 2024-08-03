from django.shortcuts import render, get_object_or_404
from .models import Author

def author_books(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = author.books.all()  # Using the related_name 'books' to get all books by the author
    return render(request, 'author_books.html', {'author': author, 'books': books})
