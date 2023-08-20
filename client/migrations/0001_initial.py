# Generated by Django 4.2.3 on 2023-08-18 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(choices=[('Oil Change', 'Oil Change'), ('Pressure Check', 'Pressure Check'), ('Cooler Change', 'Cooler Change')], max_length=50, verbose_name='Task')),
                ('task_description', models.TextField(max_length=500, verbose_name='Task description')),
                ('task_price', models.IntegerField(verbose_name='Task price')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]