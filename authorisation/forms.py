# additional functions for authorisation
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    telegram_username = forms.CharField(max_length=20, required=True, help_text='Required. Enter a valid Telegram username: @username')

    class Meta:
        model = User
        fields = ('username', 'telegram_username', 'password1', 'password2')


# from functools import wraps
# from django.http import HttpResponseForbidden
# from authorisation.views import closed_access
# #
#
# def mechanic_required(view_func):
#     @wraps(view_func)
#     def wrapped_view(request, *args, **kwargs):
#         if request.user.is_authenticated and request.user.mechanic:
#             return view_func(request, *args, **kwargs)
#         else:
#             return closed_access(request)
#
#     return wrapped_view
