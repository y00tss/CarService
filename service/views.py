from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.shortcuts import render
from service.models import ShopSupply
# from authorisation.forms import mechanic_required


# pages
@login_required
# @mechanic_required
def shop_catalog(request):
    supplies = ShopSupply.objects.all()
    return render(request, 'service/shop.html', {
        'supplies': supplies,
        'title': 'Shop'
    })


@login_required
def home(request):
    return render(request, 'service/index.html', {'title': 'Home'})


@login_required
def manuals(request):
    return render(request, 'service/manuals.html', {'title': 'Manuals'})


@login_required
def fuel(request):
    return render(request, 'service/manuals/fuel.html', {'title': 'Fuel Manual'})


@login_required
def pressure(request):
    return render(request, 'service/manuals/pressure.html', {'title': 'Pressure Test Manual'})


@login_required
def cooler(request):
    return render(request, 'service/manuals/cooler.html', {'title': 'Fill UP Manual'})


@login_required
def tasks(request):
    return render(request, 'service/tasks.html', {'title': 'Tasks'})
