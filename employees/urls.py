from django.urls import path
from . import views


urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add', views.add_employee, name='add_employee'),
    # path('employees/delete', views.employee_delete, name='employee_delete'),
]

