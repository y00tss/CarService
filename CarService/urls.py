from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from service import views as service_views
from client import views as client_views
from CarService import Sorting_Hat as Sorting_hat




urlpatterns = [
    # admin #
    path('admin/', admin.site.urls),

    #  client #
    path('order/', client_views.create_task, name='order'),


    # service & client #
    path('home/', Sorting_hat.home, name='home'),
    path('manuals/', Sorting_hat.manuals, name='manuals'),

    # service #
    path('manuals/fuel/', service_views.fuel, name='fuel'),
    path('manuals/pressure/', service_views.pressure, name='pressure'),
    path('manuals/cooler/', service_views.cooler, name='cooler'),
    path('tasks/', service_views.tasks, name='tasks'),
    path('shop/', service_views.shop_catalog, name='shop'),
    path('shop/<int:item_id>/', service_views.order_item, name='order_item'),


    # authorisation #
    path('', include('authorisation.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
