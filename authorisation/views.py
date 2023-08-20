from django.contrib.auth import login
from django.shortcuts import render, redirect
from authorisation.forms import SignUpForm


def authorisation(request):
    data = {
        'title': 'SF Car Service',
    }
    return render(request, 'authorisation/authorisation.html', data)


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
    return render(request, 'registration/registration.html', {'form': form})


def profile_view(request):
    return render(request, 'registration/profile.html', {'title': 'Profile'})


def closed_access(request):
    return render(request, 'registration/closed_access.html', {'title': 'Closed Access'})
