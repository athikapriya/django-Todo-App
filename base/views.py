from django.shortcuts import render, redirect, get_object_or_404
from .models import *


# Create your views here.
def homepage(request):
    tasks = Task.objects.all()
    context = {
        "active_page" : "homepage",
        "tasks" : tasks
    }
    return render(request, 'base/homepage.html', context)


def pending(request):
    context = {
        "active_page" : "pending"
    }
    return render(request, 'base/pending.html', context)



def overdue(request):
    context = {
        "active_page" : "overdue"
    }
    return render(request, 'base/overdue.html', context)



def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    task.is_completed = not task.is_completed
    task.save()


    context = {}
    return redirect(request.META.get('HTTP_REFERER', '/'))
