from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("<h1>This is Home page!</h1>")