from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.authorisation),
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('closed/', views.closed_access, name='closed_access'),
    path('singup/', views.signup,  name='sing'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
