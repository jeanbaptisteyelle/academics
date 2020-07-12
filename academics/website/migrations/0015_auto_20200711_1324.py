# Generated by Django 2.2.12 on 2020-07-11 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20200711_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='about_image',
            field=models.ImageField(upload_to='images/aboutsite'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='bg_autre',
            field=models.ImageField(upload_to='images/autre'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='titre_about',
            field=models.CharField(max_length=255),
        ),
    ]
