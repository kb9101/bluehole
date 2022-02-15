from tkinter.messagebox import RETRY
from django.http import HttpResponse
from organisation.models import Organisation
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.sessions.models import Session
from organisation.views import *

# Create your views here.

def main(request):
    return render(request, 'main.html')

def organisation_login(request):
    if request.session.has_key('IS_LOGIN'):
        return redirect('organisation_home')
    if request.POST:
        company_email = request.POST['email']
        password = request.POST['password']
        count = Organisation.objects.filter(company_email=company_email, password=password).count()
        if count > 0:
            request.session['IS_LOGIN']=True
            return redirect('organisation_home')
        else:
            messages.error(request, "Wrong Email or Password!")
            #return HttpResponse("Wrong ID or Password")
            return redirect('organisation_login')
    return render(request, 'organisation_login.html')

def organisation_signup(request):
    return render(request, 'organisation_signup.html')

def organisation_registration(request):
    if request.POST:
        name = request.POST['Name']
        company_email = request.POST['Email']
        password = request.POST['Password']
        contact_number = request.POST['Contact_Number']
        logo = request.POST['Logo']
        industry = request.POST['Industry']
        display_name = request.POST['Display_Name']
        description = request.POST['Description']
        country = request.POST['Country']
        city = request.POST['City']
        website = request.POST['Website']
        obj = Organisation(name=name, company_email=company_email, password=password, contact_number=contact_number, logo=logo, industry=industry, display_name=display_name, description=description, country=country, city=city, website=website)
        obj.save()
        messages.success(request,"Organisation Registration Successful!")
        return redirect('organisation_login')

    return render(request, 'organisation_signup.html')

def organisation_home(request):
    if request.session.has_key('IS_LOGIN'):
        return render(request, 'organisation_home.html')
    return redirect('organisation_login')

def organisation_logout(request):
    del request.session['IS_LOGIN']
    return redirect('organisation_login')
