
from django.conf import settings
from django.urls import path
from django.contrib import admin

from django.conf.urls.static import static
import organisation.views



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
    path('pricing/', organisation.views.pricing, name='pricing'),
    path('my_profile/', organisation.views.my_profile, name='my_profile'),
    path('settings/', organisation.views.settings, name='settings'),

    
    

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)








'''if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)'''