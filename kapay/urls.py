from django.contrib import admin
from django.urls import path, include
from employees import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('payroll/', views.payroll, name='payroll'),
    path('employees/', include('employees.urls')),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('login/', LoginView.as_view(template_name = "login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name = "logout.html"), name='logout'),
]
