# Generated by Django 4.0.2 on 2022-02-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0004_organisation_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='logo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
