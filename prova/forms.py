from pyexpat import model
from socket import fromshare
from django import forms
from .models import ProvaModel

class ProvaForm(forms.ModelForm):
    class Meta:
        model = ProvaModel
        fields = '__all__'