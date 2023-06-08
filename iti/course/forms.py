from django import forms
from .models import *

class Courseform(forms.ModelForm):
    class Meta:
       model = Courses
       fields='__all__' 