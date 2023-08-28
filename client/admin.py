from django.contrib import admin
from .models import Tasks, Userguides, UserguidesImages
# Register your models here.

admin.site.register(Tasks)
admin.site.register(Userguides)
admin.site.register(UserguidesImages)