from django import forms
from django.core import validators
from core.models import Topic,Webpage,AccessRecord




class GenForm(forms.ModelForm):
    class Meta():
        model = Webpage
        fields  = '__all__'



def checkVal(value):
    if value[0].lower() != 'a':
        raise forms.ValidationError('Pls start text with z')

class UserDetialsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea,validators=[checkVal])
