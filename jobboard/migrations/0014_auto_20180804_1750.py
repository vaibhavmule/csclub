# Generated by Django 2.0.7 on 2018-08-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0013_job_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]