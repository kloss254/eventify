# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    is_organizer = forms.BooleanField(required=False, label="Sign up as Organizer")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_organizer']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
