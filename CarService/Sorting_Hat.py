'''There are 2 same links in the navbar, but they are different for mechanic and client.'''
from django.contrib.auth.decorators import login_required
from service import views as service_views
from client import views as client_views
from authorisation.views import closed_access


@login_required
def home(request):
    if request.user.is_mechanic:
        return service_views.home(request)
    elif request.user:
        return client_views.home(request)
    else:
        return closed_access(request)


@login_required
def manuals(request):
    if request.user.is_mechanic:
        return service_views.manuals(request)
    elif request.user:
        return client_views.manuals(request)
    else:
        return closed_access(request)
