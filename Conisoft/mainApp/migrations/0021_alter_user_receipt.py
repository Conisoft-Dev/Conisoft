# Generated by Django 3.2.6 on 2021-08-17 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0020_alter_user_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='receipt',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='photo'),
        ),
    ]