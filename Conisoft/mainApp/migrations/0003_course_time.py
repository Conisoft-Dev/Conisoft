# Generated by Django 3.2.7 on 2021-10-20 21:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20211020_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
