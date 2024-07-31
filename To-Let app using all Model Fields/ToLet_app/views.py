from django.shortcuts import render, redirect # A shortcut function to render an HTML template with a given context.
from .forms import PropertyForm
from .models import Property

def property_list(request):
    properties = Property.objects.all()   # Retrieve all property objects from the database
    return render(request, 'property_list.html', {'properties': properties})    # Render the 'property_list.html' template with the properties data

def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'property_form.html', {'form': form})
