from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the task index.")

def task_list(request):
    ctx = {
        "tasks": [
            "task 1",
            "task 2",
            "task 3",
            "task 4"
        ]
    }
    return render(request, 'tasks/task_list.html', ctx)