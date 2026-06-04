from django.contrib import admin
from .models import College, Student

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'graduation_year', 'college', 'github')
    list_filter = ('graduation_year', 'college')
    search_fields = ('name', 'github')
