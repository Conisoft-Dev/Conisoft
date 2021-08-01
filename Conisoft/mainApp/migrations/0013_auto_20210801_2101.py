# Generated by Django 3.2.5 on 2021-08-01 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0012_auto_20210801_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carosel',
            name='logo',
        ),
        migrations.AddField(
            model_name='carosel',
            name='logo_image',
            field=models.ImageField(default='path/to/my/default/image.jpg', upload_to=None),
        ),
        migrations.AlterField(
            model_name='carosel',
            name='background_image',
            field=models.ImageField(upload_to=None),
        ),
    ]
