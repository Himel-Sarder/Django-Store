from django.urls import path
from .views import HelloWorldView

urlpatterns = [
    path('hello/<str:name>/', HelloWorldView.as_view(), name='hello_world'),
]
