from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "age")  # Display these fields in admin panel
    search_fields = ("name", "email")  # Add search functionality

# Alternative (without decorator):
# admin.site.register(Student, StudentAdmin)
