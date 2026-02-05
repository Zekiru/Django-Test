from django.urls import path
from .views import index, task_list, TaskListView

urlpatterns = [
    path('', index, name='index'),
    path('list', TaskListView.as_view(), name='task-list'),
]

# app_name = "task"