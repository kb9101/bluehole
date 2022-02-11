from tkinter.messagebox import RETRY
from django.http import HttpResponse
from organisation.models import Organisation
from django.contrib import messages
from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def organisation_login(request):
    if request.POST:
        company_email = request.POST['email']
        password = request.POST['password']
        count = Organisation.objects.filter(company_email=company_email, password=password).count()
        if count > 0:
            return HttpResponse("Organisation Login Successful")
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
        slug = request.POST['Slug']
        country = request.POST['Country']
        city = request.POST['City']
        website = request.POST['Website']
        obj = Organisation(name=name, company_email=company_email, password=password, contact_number=contact_number, logo=logo, industry=industry, display_name=display_name, description=description,slug=slug, country=country, city=city, website=website)
        obj.save()
        messages.success(request,"Organisation Registration Successful!")
        return redirect('organisation_login')

    return render(request, 'organisation_signup.html')