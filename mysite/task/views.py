from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import TaskGroup, Task

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# from django.http import HttpResponse

def index(request):
    return redirect('task-list')

class TaskListView(LoginRequiredMixin, TemplateView):
    template_name = 'tasks/task_list.html'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        context['taskgroups'] = TaskGroup.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        # print(request.POST.get('task_name'))
        task_name = request.POST.get('task_name')
        due_date = request.POST.get('due_date')
        taskgroup = request.POST.get('taskgroup')
        Task.objects.create(
            name=task_name,
            due_date=due_date,
            taskgroup=TaskGroup.objects.get(id=taskgroup)
        )
        return redirect('task-list')
