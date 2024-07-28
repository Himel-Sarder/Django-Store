from django.shortcuts import render, HttpResponse

def home(request):
    name = ['Himel', 'Antu', 'Abonti', 'Sana']
    container = {
        'name': name
    }
    return render(request, 'index.html', container)
