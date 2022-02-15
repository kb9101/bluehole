from curses import reset_prog_mode
from urllib import response
from xmlrpc.client import ResponseError
from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse

from organisation.views import organisation_home

# Create your tests here.

class HomePageTests(SimpleTestCase):
    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200) # this checks if the response code is equal to 200      


    # this function shows the basic working of a test case. 
    # this is made for practice only
    # this test is used for common testing purposes of any url
    def test_main_function(self):
        response = self.client.get(reverse('main'))
        self.assertEquals(response.status_code, 200) # checks if the response code is equal to 200 and if it's 200 then,  the code is working properly

    def test_correct_template(self):
        response = self.client.get(reverse('main'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_organisation_login_function(self):
        response = self.client.get(reverse('organisation_login'))
        self.assertEquals(response.status_code, 200)

    def test_organisation_login_correct_template(self):
        response = self.client.get(reverse('organisation_login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'organisation_login.html')
    
    def test_organisation_signup_function(self):
        response = self.client.get(reverse('organisation_signup'))
        self.assertEquals(response.status_code, 200)

    def test_organisation_signup_correct_template(self):
        response = self.client.get(reverse('organisation_signup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'organisation_signup.html')

    def test_organisation_registration_function(self):
        response = self.client.get(reverse('organisation_registration'))
        self.assertEquals(response.status_code, 200)