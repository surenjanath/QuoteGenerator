
from django import forms

class GenerateForm(forms.Form):

    Text = forms.CharField(
        max_length = 1000,
        widget = forms.TextInput(
            attrs={'class'          : 'fd-form-control control',
                   'placeholder'    : 'Enter Your Feedback',
                   'name'           : 'LEa8Ecb6',
                   'tabindex'       : "-1"
                   }
                               )
                           )
