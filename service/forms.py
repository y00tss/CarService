from django import forms
from client.models import Tasks
from django.forms import ModelForm

# ---------------------------------------------------EDITION FORM---------------------------------------------------
class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('task_price_job', )