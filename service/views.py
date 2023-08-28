from django.contrib.auth.decorators import login_required
from authorisation.decorations import mechanic_required
from django.shortcuts import render, redirect, get_object_or_404

from service.forms import TaskUpdateForm
from service.models import ShopSupply
from django.contrib import messages
from time import sleep
from client.models import Tasks


# pages
@login_required
@mechanic_required
def shop_catalog(request):
    supplies = ShopSupply.objects.all()
    tasks = Tasks.objects.filter(task_status=False, task_progress=True)
    return render(request, 'service/shop.html', {
        'supplies': supplies,
        'tasks': tasks,
        'title': 'Shop'
    })


@login_required
@mechanic_required
def order_item(request, item_id):
    try:
        item = ShopSupply.objects.get(pk=item_id)
    except ShopSupply.DoesNotExist:
        messages.error(request, "Item does not exist.")
        return redirect('shop')

    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Tasks, pk=task_id)

        if item.availability:
            task.task_price_equipment += item.price
            task.save()

            messages.success(request, f"Item '{item.el_name}' has been successfully ordered.")
        else:
            messages.error(request, f"Item '{item.el_name}' is not available.")

    return redirect('shop')


@login_required
def home(request):
    return render(request, 'service/index.html', {'title': 'Home'})

# ----------------------------------------MANUALS----------------------------------------
@login_required
def manuals(request):
    return render(request, 'service/manuals.html', {'title': 'Manuals'})


@login_required
@mechanic_required
def fuel(request):
    return render(request, 'service/manuals/fuel.html', {'title': 'Fuel Manual'})


@login_required
@mechanic_required
def pressure(request):
    return render(request, 'service/manuals/pressure.html', {'title': 'Pressure Test Manual'})


@login_required
@mechanic_required
def cooler(request):
    return render(request, 'service/manuals/cooler.html', {'title': 'Fill UP Manual'})

# ----------------------------------------MANUALS----------------------------------------

@login_required
@mechanic_required
def tasks(request):
    tasks_table = Tasks.objects.all()
    task_id = request.POST.get('task_id')
    user = request.user
    if request.method == 'POST':
        task = get_object_or_404(Tasks, pk=task_id)
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            task.task_price_job = form.cleaned_data['task_price_job']
            task.save()
            return redirect('tasks')

        if 'start_task' in request.POST:
            task = get_object_or_404(Tasks, pk=task_id)
            task.task_progress = True
            task.save()
            sleep(1)

        elif 'finish_task' in request.POST:
            task = get_object_or_404(Tasks, pk=task_id)
            task.task_status = True
            task.save()
            sleep(1)
    else:
        form = TaskUpdateForm()

    return render(request, 'service/tasks.html', {
        'title': 'Tasks',
        'tasks': tasks_table,
        'task_id': task_id,
        'user': user,
        'form': form})

