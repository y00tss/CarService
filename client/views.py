from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from authorisation.models import CustomUserUser
from client.models import Userguides, UserguidesImages, Tasks
from client.forms import TaskCreateForm


# Create your views here.

@login_required
def home(request):
    mechanics = CustomUserUser.objects.filter(is_mechanic=True)
    return render(request, 'client/index.html', {'title': 'Home', 'mechanics': mechanics})


@login_required
def manuals(request):
    guides = Userguides.objects.all()
    images = UserguidesImages.objects.all()
    return render(request, 'client/manuals.html', {'title': 'Manuals', 'guides': guides, 'images': images})


# @login_required
# def order(request):
#     tasks = Tasks.objects.all()
#     user = request.user
#     return render(request, 'client/order.html', {
#         'title': 'Order',
#         'tasks': tasks,
#         'user': user})


@login_required
def create_task(request):
    tasks = Tasks.objects.all()
    user = request.user
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.username = request.user
            task.save()
            return redirect('order')
    else:
        form = TaskCreateForm()

    return render(request, 'client/order.html', {
        'form': form,
        'title': 'Order',
        'tasks': tasks,
        'user': user})

