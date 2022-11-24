from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import models


user = get_user_model()


class UserLoginForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class UserRegistrationForm(UserCreationForm):
    """Class of form registration new user"""
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = user
        fields = ['username', 'email', ]
