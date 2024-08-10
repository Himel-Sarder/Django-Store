from django.urls import path
from .views import PersonDeleteView, lister


urlpatterns = [
    path('person/', lister, name='lister'),
    path('person/delete/<int:pk>/', PersonDeleteView.as_view(), name='delete'),
]
