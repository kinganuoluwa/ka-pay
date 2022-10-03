from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Employee
from .forms import UserRegisterForm, CreateEmployee


def payroll(request):
    return render(request, 'payroll.html')

def employee_list(request):
    employees = Employee.objects.all()
    context = {
        'employees':employees
    }
    return render(request, 'employee-list.html', context)

def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('employee_list')

def profile(request):
    return render(request, 'profile.html')

def change_password(request):
    return render(request, 'change-password.html')

def add_employee(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        employee_form = CreateEmployee(request.POST)
        if user_form.is_valid() and employee_form.is_valid():
            first_name = employee_form.cleaned_data.get('first_name')
            last_name = employee_form.cleaned_data.get('last_name')
            messages.success(request, f'You added {first_name} {last_name}!')
            user_form.save()
            employee_form.save()
            return redirect('employee_list')
    else:
        user_form = UserRegisterForm()
        employee_form = CreateEmployee()
    context = {
        'user_form':user_form,
        'employee_form': employee_form
    }
    return render(request, 'employee-add.html', context)
