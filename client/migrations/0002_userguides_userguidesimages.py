# Generated by Django 4.2.3 on 2023-08-25 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userguides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide_name', models.CharField(max_length=50, verbose_name='Guide name')),
                ('guide_description', models.TextField(max_length=500, verbose_name='Guide description')),
            ],
        ),
        migrations.CreateModel(
            name='UserguidesImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/guides/')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userguides')),
            ],
        ),
    ]