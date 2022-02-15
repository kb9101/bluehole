from django.db import models
# Create your models here.

class Organisation(models.Model):
    name = models.CharField(max_length=36)
    company_email = models.EmailField(max_length=36)
    password = models.CharField(max_length=36)
    contact_number = models.CharField(max_length=15)
    logo = models.ImageField(upload_to = 'images/')
    industry = models.CharField(max_length=36)
    display_name = models.CharField(max_length=36)
    description = models.CharField(max_length=250)
    country = models.CharField(max_length=36)
    city = models.CharField(max_length=36)
    website = models.URLField(max_length=250)

    def __str__(self):
        return self.name

    '''def admin_image(self):
        return '<img src="%s"/>' % self.img
    admin_image.allow_tags = True
    list_display = ('url', 'title', 'admin_image')'''




