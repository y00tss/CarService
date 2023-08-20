from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from service import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('manuals/', views.manuals, name='manuals'),
    path('manuals/fuel/', views.fuel, name='fuel'),
    path('manuals/pressure/', views.pressure, name='pressure'),
    path('manuals/cooler/', views.cooler, name='cooler'),
    path('tasks/', views.tasks, name='tasks'),
    path('shop/', views.shop_catalog, name='shop'),
    path('', include('authorisation.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
