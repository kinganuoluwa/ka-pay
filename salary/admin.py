from django.contrib import admin
from .models import Allowance, Deduction, Salary


admin.site.register(Allowance)
admin.site.register(Deduction)
admin.site.register(Salary)
