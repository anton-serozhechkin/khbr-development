from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpUserForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    email = forms.CharField(label='Электронная почта')
    password = forms.CharField(label='Пароль', widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ['username', 'email',
                'password']


class SignInUserForm(ModelForm):
    
    username = forms.CharField(label='Логин', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']