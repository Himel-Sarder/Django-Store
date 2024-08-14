from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Here, you might save the data, send an email, etc.
            return render(request, 'contact_success.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
