# Generated by Django 3.2.5 on 2021-07-30 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_attendee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendee',
            old_name='name',
            new_name='Full_Name',
        ),
        migrations.AddField(
            model_name='attendee',
            name='guest',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='Full_Name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='guest',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='industry_type',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='presenter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='reciept',
            field=models.FileField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]
