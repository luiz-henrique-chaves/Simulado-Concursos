from django import forms
from .models import ProvaModel

class ProvaForm(forms.ModelForm):
    class Meta:
        model = ProvaModel
        fields = '__all__'