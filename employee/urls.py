
from django.conf import settings
from django.urls import path

from django.conf.urls.static import static

import employee.views



urlpatterns = [
    path('employee_login/', employee.views.employee_login, name='employee_login'),
    path('employee_signup/', employee.views.employee_signup, name='employee_signup'),
    path('employee_registration/', employee.views.employee_registration, name='employee_registration'),
    path('employee_home/', employee.views.employee_home, name='employee_home'),
    path('employee_logout/', employee.views.employee_logout, name='employee_logout'),


]






