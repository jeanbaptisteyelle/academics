# Generated by Django 2.2.12 on 2020-07-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20200710_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='logo_footer',
            field=models.ImageField(null=True, upload_to='images/logo'),
        ),
    ]
