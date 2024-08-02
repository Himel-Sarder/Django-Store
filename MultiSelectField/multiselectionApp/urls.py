from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_view, name='create_view'),
    path('', views.list_view, name='list_view'),
]
