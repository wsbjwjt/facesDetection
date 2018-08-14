from django.db import models


class Employee(models.Model):

    employee_number = models.CharField(max_length=30, primary_key=True)
    employee_name = models.CharField(max_length=30)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{}:{}".format(self.employee_number, self.employee_name)


class Department(models.Model):

    department_number = models.CharField(max_length=30, primary_key=True)
    department_name = models.CharField(max_length=30)

    def __str__(self):
        return "{}:{}".format(self.department_number, self.department_name)