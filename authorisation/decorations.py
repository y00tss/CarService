from functools import wraps
from django.shortcuts import redirect
from authorisation.views import closed_access
from django.urls import reverse


def mechanic_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_mechanic:
            return view_func(request, *args, **kwargs)
        else:
            return redirect(reverse('closed_access'))

    return _wrapped_view
