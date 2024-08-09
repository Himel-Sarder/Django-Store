# myapp/urls.py
from django.urls import path
from .views import BookDetailView

urlpatterns = [
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]
