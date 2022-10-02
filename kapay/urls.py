from django.contrib import admin
from django.urls import path
from employees import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('employees/', views.employee_list, name='employee_list'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('logout/', views.logout, name='logout'),
]
