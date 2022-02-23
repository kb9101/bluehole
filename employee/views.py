import email
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render

# Create your views here.


def employee_login(request):
    if request.session.has_key('IS_LOGIN'):
        return redirect('employee_home')
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        count = Employee.objects.filter(email=email, password=password).count()
        if count > 0:
            request.session['IS_LOGIN']=True
            return HttpResponse("Employee Login Successful")
        else:
            messages.error(request, "Wrong Email or Password!")
            # return HttpResponse("Wrong ID or Password")
            return redirect('employee_login')
    return render(request, 'employee_login.html')

def employee_signup(request):
    return render(request, 'employee_signup.html') #return render(request, 'employee_signup.html')


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
        #messages.success(request, "Employee Registration Successful!")
        return redirect('employee_data') #return redirect('employee_login')

    return render(request, 'employee_signup.html') #return render(request, 'employee_signup.html')

def employee_home(request):
    if request.session.has_key('IS_LOGIN'):
        return render(request, 'employee_home.html')
    return redirect('employee_login')

def employee_logout(request):
    del request.session['IS_LOGIN']
    return redirect('employee_login')
