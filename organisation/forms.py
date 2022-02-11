from django import forms
from .models import *

class OrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ['name', 'company_email', 'password', 'contact_number', 'logo', 'industry', 'display_name', 'description', 'country', 'city', 'website']