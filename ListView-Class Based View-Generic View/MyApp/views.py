from django.shortcuts import render
from django.views.generic import ListView
from .models import item
# Create your views here.
class ItemListView(ListView):
    model = item 
    template_name = 'item_list.html'
    context_object_name = 'items'