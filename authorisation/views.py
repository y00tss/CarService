from django.contrib.auth import login
from django.shortcuts import render, redirect
from authorisation.forms import SignUpForm, ProfileEditForm
from authorisation.models import CustomUserUser

'''Registration and authorisation'''


def authorisation(request):
    mechanics = CustomUserUser.objects.filter(is_mechanic=True)
    return render(request, 'authorisation/authorisation.html', {'title': 'Authorisation', 'mechanics': mechanics})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            telegram_username = form.cleaned_data['telegram_username']
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration.html', {'form': form, 'title': 'Registration'})


'''Registration and authorisation'''

'''-----------------------------------------------------------------------------------------------------------'''

'''Profile'''


def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'profile/edit_profile.html', {'form': form, 'title': 'Edit profile'})


def profile_view(request):
    return render(request, 'registration/profile.html', {'title': 'Profile'})


'''Profile'''

'''-----------------------------------------------------------------------------------------------------------'''

'''Closed access'''


def closed_access(request):
    return render(request, 'registration/closed_access.html', {'title': 'Closed Access'})


'''Closed access'''
