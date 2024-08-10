from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Person
# Create your views here.

class PersonUpdateView(UpdateView):
    model = Person
    fields = '__all__'
    template_name = 'person_update.html'
    success_url = reverse_lazy('person_list')