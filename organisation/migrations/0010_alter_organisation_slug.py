# Generated by Django 4.0.2 on 2022-02-11 05:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0009_organisation_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]
