from django.contrib.auth.models import AbstractUser
from django.db import models

# ---------------------------------------------------CUSTOM USER---------------------------------------------------
class CustomUserUser(AbstractUser):
    is_mechanic = models.BooleanField(default=False)
    description = models.TextField(max_length=500, blank=True)
    telegram_username = models.CharField('telegram_username', max_length=20, blank=True)
    usertg_id = models.IntegerField('usertg_id', blank=True, null=True)
    avatar = models.ImageField('Images', default='no_image.jpg', upload_to='authorisation/images/profile_avatar', blank=True)

# ---------------------------------------------------CUSTOM USER---------------------------------------------------
