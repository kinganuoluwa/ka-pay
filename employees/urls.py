from django.urls import path
from . import views


urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add', views.add_employee, name='add_employee'),
    # path('employees/<int:id>/', views.employee_detail, name='employee_detail'),
    path('<int:id>/delete', views.delete_employee, name='delete_employee'),
]

