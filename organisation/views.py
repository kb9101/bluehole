import employee
from multiprocessing import context
from tkinter.messagebox import RETRY
from django.http import HttpResponse
from organisation import employee_forms
from organisation.models import Organisation
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.sessions.models import Session
from organisation.views import *
from django.conf import settings
from django.core.mail import send_mail
from .models import Organisation
from employee import models
from .employee_forms import EmployeeForm

# Create your views here.

def main(request):
    return render(request, 'main.html')

def login(request):
    if request.session.has_key('IS_LOGIN'):
        return redirect('home')
    if request.POST:
        company_email = request.POST['email']
        password = request.POST['password']
        count = Organisation.objects.filter(company_email=company_email, password=password).count()
        if count > 0:
            request.session['IS_LOGIN']=True
            return redirect('home')
        else:
            messages.error(request, "Wrong Email or Password!")
            #return HttpResponse("Wrong ID or Password")
            return redirect('login')
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def registration(request):
    if request.POST:
        name = request.POST['name']
        company_email = request.POST['email']
        password = request.POST['password']
        contact_number = request.POST['contact_number']
        logo = request.POST['logo']
        industry = request.POST['industry']
        display_name = request.POST['display_name']
        description = request.POST['description']
        country = request.POST['country']
        city = request.POST['city']
        website = request.POST['website']
        if Organisation.objects.filter(company_email=company_email).exists():
            messages.warning(request, 'Email Already Exists!')
            return redirect('signup')
        else:
            obj = Organisation(name=name, company_email=company_email, password=password, contact_number=contact_number, logo=logo, industry=industry, display_name=display_name, description=description, country=country, city=city, website=website)
            obj.is_active = False
            obj.save()
            # email_subject = 'Activate your account!'
            # email_body = ''
            subject = 'welcome to Optimus Prime'
            message = f'Hi {obj.name}, Thank You for registering in Optimus Prime.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [obj.company_email, ]
            send_mail( subject, message, email_from, recipient_list )
            # email = EmailMessage(
            #     email_subject, # the subject of the email
            #     email_body, # this is the body of the email
            #     'from@example.com',
            #     'bcc@example.com',
            #     fail_silently=False,
            #     )
            messages.success(request,"Organisation Registration Successful!")
            return redirect('login')

    return render(request, 'signup.html')

def home(request):
    if request.session.has_key('IS_LOGIN'):
        return render(request, 'home.html')
    return redirect('login')

def logout(request):
    del request.session['IS_LOGIN']
    return redirect('login')

def blocks(request):
    return render(request, 'blocks.html')

def cards(request):
    return render(request, 'cards.html')

def carousels(request):
    return render(request, 'carousels.html')

def forms(request):
    return render(request, 'forms.html')

def people(request):
    return render(request, 'people.html')

def employee_data(request):
    employee = models.Employee.objects.all()
    return render(request, 'employee_data.html', {'employee':employee})

def my_profile(request):
    company_email = request.session.get('company_email')
    details = Organisation.objects.filter(company_email = 'kushbhatia@gmail.com')
    return render(request, 'my_profile.html', {'details':details})

def settings(request):
    return render(request, 'settings.html')

def edit_employee_data(request, id):
    employee = models.Employee.objects.get(id=id)
    return render(request, 'edit_employee_data.html', {'employee':employee})

def update_employee_data(request, id):
    employee = models.Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    form.save()
    return redirect('employee_data')

# add employee start

def load_employee_form(request):
    form = EmployeeForm
    return render(request, 'employee_signup.html', {'form':form})

def add_employee_data(request):
    form = EmployeeForm(request.POST)
    form.save()
    return redirect('/employee_data')

# add employee end


def delete_employee_data(request, id):
    employee = models.Employee.objects.get(id=id)
    employee.delete()
    return redirect('employee_data')