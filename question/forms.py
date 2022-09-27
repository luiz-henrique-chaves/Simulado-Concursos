from dataclasses import fields
from django import forms
from .models import QuestionModel

class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionModel
        fields = '__all__'
