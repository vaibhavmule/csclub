# Generated by Django 2.0.7 on 2018-08-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0017_auto_20180809_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employmenttype',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
