# additional functions for authorisation
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from authorisation.models import CustomUserUser

# ------------------------------------------------Registration FORM------------------------------------------------


class SignUpForm(UserCreationForm):
    telegram_username = forms.CharField(max_length=20, required=True,
                                        help_text='Required. Enter a valid Telegram username: @username')

    class Meta:
        model = CustomUserUser
        fields = ('username', 'telegram_username', 'password1', 'password2')

# ------------------------------------------------Registration FORM------------------------------------------------


# ---------------------------------------------------EDITION FORM---------------------------------------------------


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUserUser
        fields = ('avatar', 'first_name', 'last_name', 'telegram_username', 'email', 'description')


# ---------------------------------------------------EDITION FORM---------------------------------------------------