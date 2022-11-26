from django.forms import ModelForm
from .models import Task, TaskGroup


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'text', 'complete_date', ]


class TaskGroupCreateForm(ModelForm):
    class Meta:
        model = TaskGroup
        fields = ['group_name', 'tasks', ]
