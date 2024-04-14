from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
# Create your views here.

def add_task(request):
    add_task = request.POST['task']
    Tasks.objects.create(task=add_task)
    return redirect('home')

def mark_as_done(request, id):
    task = get_object_or_404(Tasks, pk=id)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, id):
    task = get_object_or_404(Tasks, pk=id)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, id):
    get_task = get_object_or_404(Tasks, pk=id)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        return render(request, 'edit.html', {'get_task':get_task})

def delete_task(request, id):
    get_task = get_object_or_404(Tasks, pk=id)
    get_task.delete()
    return redirect('home')
