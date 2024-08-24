from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):

    # Use of initial in django

    initials = {
        'name': 'My name is ',
        'email': '@gmail.com',
        'message': 'Hello'
    }
    if request.method == 'POST':
        form = ContactForm(request.POST, initial=initials)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Here, you might save the data, send an email, etc.
            return render(request, 'contact_success.html', {'form': form})
    else:
        form = ContactForm(initial=initials)

    return render(request, 'contact.html', {'form': form})
