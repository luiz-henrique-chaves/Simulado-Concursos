from dataclasses import fields
from django import forms
from .models import DisciplinaModel

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = DisciplinaModel
        fields = '__all__'