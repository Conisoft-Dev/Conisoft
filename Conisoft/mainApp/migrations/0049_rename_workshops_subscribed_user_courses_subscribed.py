# Generated by Django 3.2.6 on 2021-09-01 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0048_course_max_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='workshops_subscribed',
            new_name='courses_subscribed',
        ),
    ]
