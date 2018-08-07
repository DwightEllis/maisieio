from django import forms

from .models import IO

class IOForm(forms.ModelForm):

    class Meta:
        model = IO
        fields = ('input_type', 'quantity','event_date', 'note',)