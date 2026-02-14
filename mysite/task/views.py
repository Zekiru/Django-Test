from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import TaskGroup, Task

# Create your views here.

from django.http import HttpResponse

tasks: list[str] = ["task 1", "task 2", "task 3", "task 4"]

def index(request):
    return redirect('task-list')

def task_list(request):
    ctx = {"tasks": tasks}
    if request.method == "POST":
        print(request.POST.get('task_name'))
        ctx["tasks"].append(request.POST.get('task_name'))
    return render(request, 'tasks/task_list.html', ctx)

class TaskListView(TemplateView):
    template_name = 'tasks/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        # print(request.POST.get('task_name'))
        task_name = request.POST.get('task_name')
        if task_name:
            Task.objects.create(
                name=task_name,
                due_date="2026-12-31T23:59:59",
                taskgroup=TaskGroup.objects.first()   # Assuming there is at least one TaskGroup
            )
        context = self.get_context_data(**kwargs)
        return self.get(request, *args, **kwargs)
