
from os import name
from django.conf import settings
from django.urls import path
from django.contrib import admin

from django.conf.urls.static import static
import organisation.views
from employee import models 



urlpatterns = [

    path('login/', organisation.views.login, name='login'),
    path('signup/', organisation.views.signup, name='signup'),
    path('registration/', organisation.views.registration, name='registration'),
    path('logout/', organisation.views.logout, name='logout'),
    path('home/', organisation.views.home, name='home'),
    path('blocks/', organisation.views.blocks, name='blocks'),
    path('cards/', organisation.views.cards, name='cards'),
    path('carousels/', organisation.views.carousels, name='carousels'),
    path('forms/', organisation.views.forms, name='forms'),
    path('people/', organisation.views.people, name='people'),
    path('employee_data/', organisation.views.employee_data, name='employee_data'),
    path('my_profile/', organisation.views.my_profile, name='my_profile'),
    path('settings/', organisation.views.settings, name='settings'),
    path('employee_data/edit_employee_data/<int:id>',organisation.views.edit_employee_data, name='edit_employee_data'),
    path('update_employee_data/<int:id>',organisation.views.update_employee_data, name='update_employee_data'),
    path('employee_data/delete_employee_data/<int:id>',organisation.views.delete_employee_data, name='delete_employee_data'),
    path('employee_data/add_employee_data/',organisation.views.add_employee_data, name='add_employee_data'),
    path('load_employee_form/',organisation.views.load_employee_form, name='load_employee_form'),


    
    

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)








'''if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)'''