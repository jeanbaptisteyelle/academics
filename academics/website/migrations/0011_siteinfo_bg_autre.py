# Generated by Django 2.2.12 on 2020-07-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20200710_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='bg_autre',
            field=models.ImageField(null='True', upload_to='images/caracteristique'),
            preserve_default='True',
        ),
    ]
