# Generated by Django 4.2.3 on 2023-08-27 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_userguides_userguidesimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userguidesimages',
            name='image',
            field=models.ImageField(upload_to='client/guised/images/'),
        ),
    ]