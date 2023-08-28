from django import forms
from client.models import Tasks
from django.forms import ModelForm


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('task_name', 'task_description')



