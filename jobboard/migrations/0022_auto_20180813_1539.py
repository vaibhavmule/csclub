# Generated by Django 2.0.7 on 2018-08-13 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0021_auto_20180813_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='apply_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='apply_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]