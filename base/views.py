from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import TaskForm
from .filters import TaskFilter

# Create your views here.
def homepage(request):
    tasks = Task.objects.filter(is_completed=False)
    
    completed_tasks = Task.objects.filter(is_completed=True)

    myFilter = TaskFilter(request.GET, queryset = tasks)
    tasks = myFilter.qs

    context = {
        "active_page" : "homepage",
        "tasks" : tasks,
        "completed_tasks" : completed_tasks,
        "myFilter" : myFilter
    }
    return render(request, 'base/homepage.html', context)


def pending(request):
    time = timezone.now()
    pending_tasks = Task.objects.filter(deadline__gte=time, is_completed=False)
    context = {
        "active_page" : "pending",
        "pending_tasks" : pending_tasks
    }
    return render(request, 'base/pending.html', context)



def overdue(request):
    time = timezone.now()
    overdue_tasks = Task.objects.filter(deadline__lt=time, is_completed=False)
    context = {
        "active_page" : "overdue",
        "overdue_tasks" : overdue_tasks
    }
    return render(request, 'base/overdue.html', context)



def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    task.is_completed = not task.is_completed
    task.save()


    context = {}
    return redirect(request.META.get('HTTP_REFERER', '/'))



def create_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")

    context = {
        'form' : form
    }
    return render(request, 'base/task_form.html', context)




def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    context = {
        "form" : form
    }
    return render(request, 'base/task_form.html', context)



def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect("/")
    context = {
        'task' : task
    }
    return render(request, 'base/delete_task.html', context)
