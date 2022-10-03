from django.shortcuts import render, redirect
from .models import Employee
from .forms import UserRegisterForm, CreateEmployee


def dashboard(request):
    return render(request, 'dashboard.html')

def employee_list(request):
    employees = Employee.objects.all()
    context = {
        'employees':employees
    }
    return render(request, 'employee-list.html', context)

# def employee_delete(request):
#     return render(request, 'employee-list.html')

def profile(request):
    return render(request, 'profile.html')

def change_password(request):
    return render(request, 'change-password.html')

def employee_add(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        employee_form = CreateEmployee(request.POST)
        if user_form.is_valid() and employee_form.is_valid():
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
