from django.urls import path
from .views import PersonUpdateView

urlpatterns = [
    path('person/update/<int:pk>/', PersonUpdateView.as_view(), name='person_update'),
]
