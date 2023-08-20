from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserUser(AbstractUser):
    is_mechanic = models.BooleanField(default=False)
    description = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField('Images', default='no_image.jpg', upload_to='authorisation/images/mechanics', blank=True)
