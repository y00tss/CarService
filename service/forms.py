from django import forms
from client.models import Tasks
from django.forms import ModelForm


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('task_price_job', )