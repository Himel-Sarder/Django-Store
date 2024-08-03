from django.urls import path
from . import views

urlpatterns = [
    path('author/<int:author_id>/books/', views.author_books, name='author_books'),
]
