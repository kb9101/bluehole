import email
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
            return redirect('organisation_signup')
        else:
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

def pricing(request):
    return render(request, 'pricing.html') 