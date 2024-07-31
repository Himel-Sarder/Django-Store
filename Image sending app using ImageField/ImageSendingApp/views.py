from django.shortcuts import render, redirect
from .forms import MyModelForm

def index(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MyModelForm()
    
    return render(request, 'index.html', {'form': form})
