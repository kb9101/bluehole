# Generated by Django 4.0.2 on 2022-02-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0012_alter_organisation_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
