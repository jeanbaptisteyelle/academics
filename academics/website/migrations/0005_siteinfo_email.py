# Generated by Django 2.2.12 on 2020-07-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_caracteristique_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
