# Generated by Django 3.2.6 on 2021-08-28 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0036_auto_20210828_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='taken_slots',
            field=models.IntegerField(default=0),
        ),
    ]