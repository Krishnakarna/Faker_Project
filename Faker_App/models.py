from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    salary = models.FloatField()
    mobile = models.BigIntegerField(unique=True,blank=True,null=True)

    def __str__(self):
        return self.first_name
