from django import forms

class ConnectionForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(max_length=20, required=False)