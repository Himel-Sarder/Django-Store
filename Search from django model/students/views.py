from django.shortcuts import render
from .models import Student
from django.db.models import Q
from django.shortcuts import redirect

def home(request):
    return redirect("search_students")  # Redirects to the search page

def search_students(request):
    query = request.GET.get("q")
    students = Student.objects.all()

    if query:
        students = students.filter(Q(name__icontains=query) | Q(email__icontains=query))
        

    return render(request, "students/search.html", {"students": students})
