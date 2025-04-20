from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
# from .models import Employee
# from .forms import EmployeeForm
from time import time

def hr_view(request):
    return render(request, 'hr_management/hr.html')

def manage_employee(request):
    if request.method == 'GET':
        action = request.GET.get('action')
        if not action:
            return render(request, 'hr.html', {'time': int(time())})
        
        if action == 'check_code':
            code = request.GET.get('code')
            try:
                emp = Employee.objects.get(code=code)
                return JsonResponse({
                    'exists': True,
                    'photo': emp.photo.url if emp.photo else '',
                    'code': emp.code,
                    'login': emp.login,
                    'name': emp.name,
                    'phone': emp.phone,
                    'email': emp.email,
                    'cpf': emp.cpf,
                    'birth_day': str(emp.birth_date.day).zfill(2),
                    'birth_month': str(emp.birth_date.month).zfill(2),
                    'birth_year': str(emp.birth_date.year),
                    'gender': emp.gender,
                    'marital_status': emp.marital_status,
                    'address': emp.address,
                    'cep': emp.cep,
                    'academic_formation': emp.academic_formation,
                    'salary': float(emp.salary),
                    'department': emp.department,
                    'position': emp.position,
                    'benefits1': emp.benefits1,
                    'benefits2': emp.benefits2,
                    'benefits3': emp.benefits3,
                    'benefits4': emp.benefits4,
                    'benefits5': emp.benefits5,
                    'benefits6': emp.benefits6,
                    'benefits7': emp.benefits7,
                    'benefits8': emp.benefits8,
                    'benefits9': emp.benefits9,
                    'benefits10': emp.benefits10,
                    'admission_day': str(emp.admission_date.day).zfill(2),
                    'admission_month': str(emp.admission_date.month).zfill(2),
                    'admission_year': str(emp.admission_date.year),
                    'status': emp.status,
                    'inactive_status': emp.inactive_status,
                    'date_of_dismissal_day': str(emp.date_of_dismissal_date.day).zfill(2) if emp.date_of_dismissal_date else " none",
                    'date_of_dismissal_month': str(emp.date_of_dismissal_date.month).zfill(2) if emp.date_of_dismissal_date else " none",
                    'date_of_dismissal_year': str(emp.date_of_dismissal_date.year) if emp.date_of_dismissal_date else " none"
                })
            except Employee.DoesNotExist:
                return JsonResponse({'exists': False})

        if action == 'list_employees':
            employees = Employee.objects.all().order_by('name')
            data = []
            for emp in employees:
                data.append({
                    'photo': emp.photo.url if emp.photo else '',
                    'code': emp.code,
                    'login': emp.login,
                    'name': emp.name,
                    'department': emp.department,
                    'position': emp.position,
                    'status': emp.status
                })
            return JsonResponse({'employees': data})

    elif request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save()
            return JsonResponse({'success': True, 'message': 'Funcionário salvo com sucesso!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
