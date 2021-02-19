from django.db import models

class Employee(models.Model):
    employee_id = models.IntegerField(null=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    job_title = models.CharField(null=True,max_length=30)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)

    def get_absolute_url(self):
        return reverse('EmployeeList:emp_detail_view', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
    

