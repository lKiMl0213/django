from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm

def employee_list(request):
    employees = Employee
    return render(request, "employee_list.html", {"employees": employees})

def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee created successfully.")
            return redirect("employee_list")
    else:
        form = EmployeeForm()
    return render(request, "employee_form.html", {"form": form})

def employee_update(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully.")
            return redirect("employee_list")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "employee_form.html", {"form": form})

