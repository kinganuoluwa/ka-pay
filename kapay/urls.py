from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from employees import views
from employees.views import HomeView, PayrollView, ProfileView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('payroll/', PayrollView.as_view(), name='payroll'),
    path('employees/', include('employees.urls')),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('login/', LoginView.as_view(template_name = "login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name = "logout.html"), name='logout'),
]
