# Generated by Django 3.2.6 on 2021-09-03 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0052_auto_20210901_2219'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Edition',
        ),
        migrations.DeleteModel(
            name='PaperRequirement',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
