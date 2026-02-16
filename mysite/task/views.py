from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import TaskGroup, Task

# Create your views here.

from django.http import HttpResponse

def index(request):
    return redirect('task-list')

class TaskListView(TemplateView):
    template_name = 'tasks/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        # print(request.POST.get('task_name'))
        task_name = request.POST.get('task_name')
        Task.objects.create(
            name=task_name,
            due_date="2026-12-31T23:59:59",
            taskgroup=TaskGroup.objects.first()   # Assuming there is at least one TaskGroup
        )
        return redirect('task-list')
