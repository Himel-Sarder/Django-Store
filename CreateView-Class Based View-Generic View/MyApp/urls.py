# myapp/urls.py
from django.urls import path
from django.views.generic import TemplateView
from .views import PersonCreateView

urlpatterns = [
    path('add/', PersonCreateView.as_view(), name='add_person'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='person_success'),
]
