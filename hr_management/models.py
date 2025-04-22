from django.shortcuts import render
from django.db import models
from users.models import Employee

def employee_list_view(request):
    employees = Employee.objects.filter(statsus='active')
    return render(request, 'hr_management/employee_list.html', {'employees': employees})