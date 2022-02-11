from os import name
from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=36)
    email = models.EmailField(max_length=36)
    password = models.CharField(max_length=36)
    contact_number = models.CharField(max_length=36)
    country = models.CharField(max_length=36)
    city = models.CharField(max_length=36)

    def __str__(self):
        return self.name
    

