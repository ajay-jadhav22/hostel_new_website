from django import forms
from .models import Application

# Form for Student model

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields =  '__all__'