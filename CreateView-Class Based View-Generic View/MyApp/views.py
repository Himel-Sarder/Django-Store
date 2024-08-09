# myapp/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Person

class PersonCreateView(CreateView):
    model = Person
    fields = ['name']
    template_name = 'form.html'
    success_url = reverse_lazy('person_success')
