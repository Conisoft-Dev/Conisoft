# Generated by Django 3.2.6 on 2021-09-01 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0050_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='None/conisoft_logo_0SeqbbO.png', upload_to=None),
        ),
    ]