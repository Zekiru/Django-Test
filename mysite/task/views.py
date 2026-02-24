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
        return context

    def post(self, request, *args, **kwargs):
        # print(request.POST.get('task_name'))
        task_name = request.POST.get('task_name')
        Task.objects.create(
            name=task_name,
            due_date="2026-12-31T23:59:59",
            taskgroup=TaskGroup.objects.first()
        )
        return redirect('task-list')
