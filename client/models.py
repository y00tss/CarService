from django.db import models
from django.conf import settings

# Create your models here.
'''-----------------------------------------------------------------------'''
'''---------------------------TASK MODELS---------------------------------'''


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
    task_price_job = models.IntegerField('Task price', default=0)
    task_price_equipment = models.IntegerField('Equipment price', default=0)
    task_status = models.BooleanField('Task status', default=False)
    task_progress = models.BooleanField('Task progress', default=False)

    def __str__(self):
        return self.task_name

    def total_price(self):
        return self.task_price_job + self.task_price_equipment

    def start_task(self):
        self.task_progress = True
        self.save()

    def finish_task(self):
        self.task_status = True
        self.save()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


'''-----------------------------------------------------------------------'''
'''---------------------------SHOP MODELS---------------------------------'''


class Userguides(models.Model):
    # fields
    guide_name = models.CharField('Guide name', max_length=50)
    guide_description = models.TextField('Guide description', max_length=500)


class UserguidesImages(models.Model):
    guide = models.ForeignKey(Userguides, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='client/guised/images/')
