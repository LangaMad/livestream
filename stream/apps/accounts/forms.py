from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone',
                  'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
        'placeholder': 'Username'}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control',
        'placeholder': 'Email'}))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
        'placeholder': 'Password'}))





