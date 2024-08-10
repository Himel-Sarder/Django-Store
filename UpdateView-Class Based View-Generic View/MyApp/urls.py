from django.urls import path
from .views import PersonUpdateView
from .views import person_list

urlpatterns = [
    path('person/update/<int:pk>/', PersonUpdateView.as_view(), name='person_update'),
    path('persons/', person_list, name='person_list'),
]
