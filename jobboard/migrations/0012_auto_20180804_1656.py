# Generated by Django 2.0.7 on 2018-08-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0011_auto_20180804_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='logo',
            field=models.ImageField(default='default.jpg', upload_to='logo/'),
        ),
    ]
