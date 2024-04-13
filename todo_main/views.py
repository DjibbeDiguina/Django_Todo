from django.shortcuts import render
from todo.models import Tasks

def home(request):
    task = Tasks.objects.filter(is_completed=False)

    completed_task = Tasks.objects.filter(is_completed = True)

    return render(request, 'home.html',{'tasks':task, 'completed_task':completed_task})