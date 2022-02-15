
from django.conf import settings
from django.urls import path
from django.contrib import admin

from django.conf.urls.static import static
import organisation.views



urlpatterns = [

    path('organisation_login/', organisation.views.organisation_login, name='organisation_login'),
    path('organisation_signup/', organisation.views.organisation_signup, name='organisation_signup'),
    path('organisation_registration/', organisation.views.organisation_registration, name='organisation_registration'),
    path('organisation_logout/', organisation.views.organisation_logout, name='organisation_logout'),
    path('organisation_home/', organisation.views.organisation_home, name='organisation_home'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)








'''if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)'''