from django import forms
from .models import Task

class Taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields= '__all__'
        widgets = {
            'due_date':forms.DateInput(attrs={'type':'date'})
    
       }

