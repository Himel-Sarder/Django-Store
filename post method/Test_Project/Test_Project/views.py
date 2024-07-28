# views.py
from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Process the form data (e.g., save to database, send email)
        print(name)
        print(email)
        print(message)
        
        # Here we just return a simple HTTP response for demonstration
        return HttpResponse(f'<h1>Thank you, {name}! Your message has been received.</h1>')
    return render(request, 'contact.html')
