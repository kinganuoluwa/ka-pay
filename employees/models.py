from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    date_joined = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Salary(models.Model):
    pass
