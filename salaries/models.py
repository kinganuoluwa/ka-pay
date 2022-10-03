from django.db import models
from employees.models import Employee


class Salary(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    basic_salary = models.FloatField()
    
    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name}'s Salary"
