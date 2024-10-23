from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'position', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email', 'department')

admin.site.register(Employee, EmployeeAdmin)
