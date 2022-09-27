from pyexpat import model
from socket import fromshare
from django import forms
from .models import AnswerModel

class AnswerForm(forms.ModelForm):
    class Meta:
        model = AnswerModel
        fields = '__all__'