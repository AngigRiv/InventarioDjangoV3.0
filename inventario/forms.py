from django import forms 

from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        max_length=65,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )