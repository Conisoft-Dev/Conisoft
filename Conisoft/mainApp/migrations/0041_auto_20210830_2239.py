# Generated by Django 3.2.6 on 2021-08-30 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0040_auto_20210830_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='receipt_1',
            field=models.ImageField(blank=True, null=True, upload_to='receipts', verbose_name='Receipt_1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='receipt_2',
            field=models.ImageField(blank=True, null=True, upload_to='receipts', verbose_name='Receipt_2'),
        ),
    ]
