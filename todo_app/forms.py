
from .models import todo
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model=todo
        fields= '__all__'