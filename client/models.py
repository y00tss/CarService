from django.db import models
from django.conf import settings


# Create your models here.

class Tasks(models.Model):
    jobs = (
        ('Oil Change', 'Oil Change'),
        ('Pressure Check', 'Pressure Check'),
        ('Cooler Change', 'Cooler Change'),
    )

    # fields
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    task_name = models.CharField('Task', max_length=50, choices=jobs)
    task_description = models.TextField('Task description', max_length=500)
    task_price = models.IntegerField('Task price')

    def __str__(self):
        return self.task_name

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
