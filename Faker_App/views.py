from django.shortcuts import render,redirect
from django.http import HttpResponse
from Faker_App.models import Employee


from faker import Faker
fake=Faker()

def EmployeeFakeData(required):
    for i in range(50):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        city = fake.city()
        role = fake.random_element(elements=('SE','TL','MGR','PM'))
        salary = fake.random_element(elements=(10000,20000,30000,40000,50000))
        mobile = fake.random_int(min=9000,max=999999)


        Employee.objects.create(
            first_name=first_name,last_name=last_name,email=email,city=city,role=role,salary=salary,mobile=mobile
        )
        return redirect('display_fake_data/')

def EmployeeDisplayData(request):
    employee_list=Employee.objects.all()
    employee_count=Employee.objects.count()
    manager_count=Employee.objects.filter(role='SE').count()
    context={
        'employee_list':employee_list,
        'employee_count':employee_count,
        'manager_count':manager_count,

    }
    return render(request,'employee_display.html',context)