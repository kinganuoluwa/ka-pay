from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from .models import Employee
from .forms import CreateEmployee


class HomeView(TemplateView):
    template_name = 'home.html'

# def home(request):
#     return render(request, 'home.html')
class PayrollView(LoginRequiredMixin, TemplateView):
    template_name = 'payroll.html'

# @login_required
# def payroll(request):
#     return render(request, 'payroll.html')

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employee-list.html'
    context_object_name = 'employees'

# @login_required
# def employee_list(request):
#     employees = Employee.objects.all()
#     context = {
#         'employees':employees
#     }
#     return render(request, 'employee-list.html', context)

@login_required
def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    message = messages.error(request, f'You deleted an Employee')
    return redirect('employee-list')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

# @login_required
# def profile(request):
#     return render(request, 'profile.html')

@login_required
def change_password(request):
    return render(request, 'change-password.html')

@login_required
def add_employee(request):
    if request.method == 'POST':
        employee_form = CreateEmployee(request.POST)
        if employee_form.is_valid():
            first_name = employee_form.cleaned_data.get('first_name')
            last_name = employee_form.cleaned_data.get('last_name')
            messages.success(request, f'You added {first_name} {last_name}!')
            employee_form.save()
            return redirect('employee-list')
    else:
        employee_form = CreateEmployee()
    context = {
        'employee_form': employee_form
    }
    return render(request, 'employee-add.html', context)
