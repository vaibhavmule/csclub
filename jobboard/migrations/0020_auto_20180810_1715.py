# Generated by Django 2.0.7 on 2018-08-10 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0019_auto_20180810_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
