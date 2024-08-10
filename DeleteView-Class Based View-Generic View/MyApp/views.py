from django.shortcuts import render
from .models import Person
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
# Create your views here.
class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'confirmation.html'
    success_url = reverse_lazy('lister')

def lister(request):
    people = Person.objects.all()
    return render(request, 'lister.html', {'people': people})