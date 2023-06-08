from django import forms
from django.contrib.auth.models import *
from .models import *
class RegistrationAdminform(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'style':'color:red'
    }))
    username = forms.CharField()
    password = forms.CharField(label='Password',widget=forms.PasswordInput,max_length=12,required=False)


class RegistrationAdminformModel(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Myuser
        # fields='__all__'
        exclude= ['password']