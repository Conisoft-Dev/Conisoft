# Generated by Django 3.2.6 on 2021-08-17 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0022_alter_user_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='paper',
            field=models.FileField(blank=True, null=True, upload_to='papers', verbose_name='document'),
        ),
        migrations.AlterField(
            model_name='user',
            name='receipt',
            field=models.ImageField(blank=True, null=True, upload_to='receipts', verbose_name='photo'),
        ),
    ]