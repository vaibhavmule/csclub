# Generated by Django 2.0.7 on 2018-08-01 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0003_auto_20180801_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
