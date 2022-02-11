import email
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render

# Create your views here.


def employee_login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        count = Employee.objects.filter(email=email, password=password).count()
        if count > 0:
            return HttpResponse("Employee Login Successful")
        else:
            messages.error(request, "Wrong Email or Password!")
            # return HttpResponse("Wrong ID or Password")
            return redirect('employee_login')
    return render(request, 'employee_login.html')


def employee_signup(request):
    return render(request, 'employee_signup.html')


def employee_registration(request):
    if request.POST:
        name = request.POST['Name']
        email = request.POST['Email']
        password = request.POST['Password']
        contact_number = request.POST['Contact_Number']
        country = request.POST['Country']
        city = request.POST['City']
        obj = Employee(name=name, email=email, password=password,
                       contact_number=contact_number, country=country, city=city)
        obj.save()
        messages.success(request, "Employee Registration Successful!")
        return redirect('employee_login')

    return render(request, 'employee_signup.html')
