# Generated by Django 2.2.12 on 2020-07-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_siteinfo_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinfo',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='slogan',
            field=models.CharField(max_length=255),
        ),
    ]
