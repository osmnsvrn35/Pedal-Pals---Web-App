from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinLengthValidator


class RegistrationForm(forms.Form):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, validators=[
        RegexValidator(r'^[a-zA-Z\s]*$', 'First name should not contain numbers.')
    ])
    last_name = forms.CharField(required=True, validators=[
        RegexValidator(r'^(?:(?![0-9])[a-zA-Z])+$', 'Last name should not contain numbers.')
    ])
    password = forms.CharField(widget=forms.PasswordInput, validators=[
        RegexValidator(
            regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[?*.])[A-Za-z\d?*.]{8,}$',
            message='Password must contain at least one capital letter, one number and at least one of the following '
                    'special characters: ?, *, . and must be at least 8 characters long.'
        )
    ])
    username = forms.CharField(required=True)
    age = forms.IntegerField(required=False)
    phone_number = forms.CharField(required=False)
    address = forms.CharField(required=False)
    widgets = {   
            "password": forms.PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password'}),
    }

class LoginForm(forms.Form):
    username = forms.EmailField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput)