from django.contrib import admin
from .models import TaskGroup, Task

# Register your models here.

admin.site.register(TaskGroup)
admin.site.register(Task)
