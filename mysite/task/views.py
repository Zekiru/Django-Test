from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

from django.http import HttpResponse

tasks: list[str] = ["task 1", "task 2", "task 3", "task 4"]

def index(request):
    return HttpResponse("Hello, world. You're at the task index.")

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
        context['tasks'] = tasks
        return context

    def post(self, request, *args, **kwargs):
        # print(request.POST.get('task_name'))
        tasks.append(request.POST.get('task_name'))
        context = self.get_context_data(**kwargs)
        return self.get(request, *args, **kwargs)
