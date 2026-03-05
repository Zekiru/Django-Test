from django import forms

from .models import TaskGroup

class TaskForm(forms.Form):
    task_name = forms.CharField(
        label='Task Name',
        max_length=100,
    )
    due_date = forms.DateTimeField(
        label='Due Date',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    taskgroup = forms.ModelChoiceField(
        queryset=TaskGroup.objects.all(),
        label='Task Group',
    )