# Generated by Django 2.2.12 on 2020-07-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20200710_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinfo',
            name='description_footer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='logo_footer',
            field=models.ImageField(upload_to='images/logofooter'),
        ),
    ]
