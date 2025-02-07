from django.urls import path
from .views import search_students, home

urlpatterns = [
    path("", home, name="home"),  # Homepage that redirects to search
    path("search/", search_students, name="search_students"),
]

