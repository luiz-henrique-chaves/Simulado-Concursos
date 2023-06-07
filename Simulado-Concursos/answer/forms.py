from pyexpat import model
from django import forms
from .models import AnswerModel

class AnswerForm(forms.ModelForm):
    class Meta:
        model = AnswerModel
        fields = '__all__'
        widgets = {
            'a': forms.Textarea(attrs={'class':'form-control', 'rows':'1'}),
            'b': forms.Textarea(attrs={'class':'form-control', 'rows':'1'}),
            'c': forms.Textarea(attrs={'class':'form-control', 'rows':'1'}),
            'd': forms.Textarea(attrs={'class':'form-control', 'rows':'1'}),
            'explanation': forms.Textarea(attrs={'class':'form-control', 'rows':'2'}),
            'question': forms.HiddenInput(attrs=None),
        }