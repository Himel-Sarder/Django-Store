from django.shortcuts import render, redirect
from .forms import MyModelForm
from .models import MyModel

# Create your views here.
def create_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_view')
    else:
        form = MyModelForm()
    return render(request, 'create.html', {'form': form})

def list_view(request):
    items = MyModel.objects.all()
    return render(request, 'list.html', {'items': items})

    
