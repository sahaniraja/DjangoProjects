# Generated by Django 3.2.8 on 2021-10-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcodeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrcode',
            name='url',
        ),
        migrations.AddField(
            model_name='qrcode',
            name='Qrtxt',
            field=models.CharField(default='', max_length=500),
        ),
    ]