# from django import forms
from django.forms import ModelForm

from .models import IO

class IOForm(ModelForm):

    class Meta:
        model = IO
        fields = ['input_type', 'quantity','event_date', 'note', 'urineFlag', 
            'poopFlag','test']