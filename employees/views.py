from django.shortcuts import render


def dashboard(request):
    return render(request, 'dashboard.html')

def employee_list(request):
    return render(request, 'employee-list.html')

def employee_add(request):
    return render(request, 'employee-add.html')

# def employee_delete(request):
#     return render(request, 'employee-list.html')

def profile(request):
    return render(request, 'profile.html')

def change_password(request):
    return render(request, 'change-password.html')

def logout(request):
    return render(request, 'logout.html')
