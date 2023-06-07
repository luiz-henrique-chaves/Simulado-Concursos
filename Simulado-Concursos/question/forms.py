from django import forms
from .models import QuestionModel

class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionModel
        fields = '__all__'
        widgets = {
            'issue': forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
        }
