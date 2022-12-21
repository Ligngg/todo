from .models import Task
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['task1','priority1','date1']