from django.test import TestCase
from .models import Employee

# Create your tests here.

class EmployeeTestCase(TestCase):
    def setUp(self):
        Employee.objects.create(name = 'Kush', email = 'k@gmail.com', password = '12345', contact_number = 1234567890, country = 'India', city = 'Ahmedabad')
        Employee.objects.create(name = 'Bhatia', email = 'b@gmail.com', password = '54321', contact_number = 9876543210, country = 'USA', city = 'New York')

    def test_employee_test(self):
        employee1 = Employee.objects.get(name = 'Kush', email = 'k@gmail.com', password = '12345', contact_number = 1234567890, country = 'India', city = 'Ahmedabad')
        employee2 = Employee.objects.get(name = 'Bhatia', email = 'b@gmail.com', password = '54321', contact_number = 9876543210, country = 'USA', city = 'New York')
        self.assertEqual(employee1.name, 'Kush')
        self.assertEqual(employee2.name, 'Bhatia')