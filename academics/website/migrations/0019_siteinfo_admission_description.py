# Generated by Django 2.2.12 on 2020-07-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20200711_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='admission_description',
            field=models.TextField(null='True'),
            preserve_default='True',
        ),
    ]