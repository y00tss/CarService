# Generated by Django 4.2.3 on 2023-08-27 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_alter_tasks_task_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task_price',
            field=models.IntegerField(default=0, verbose_name='Task price'),
        ),
    ]
