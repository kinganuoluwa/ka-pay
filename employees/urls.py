from django.urls import path
from . import views


urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add', views.employee_add, name='employee_add'),
    # path('employees/delete', views.employee_delete, name='employee_delete'),
]

